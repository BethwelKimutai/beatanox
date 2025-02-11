import uuid
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

# Base Model
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class GenericBaseModel(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True  # <-- Mark the model as abstract


class TransactionType(GenericBaseModel):
    simple_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)

    def  __str__(self):
        return self.name

class Transaction(GenericBaseModel):
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, related_name="logs")
    source_ip = models.GenericIPAddressField()
    request = models.TextField()
    transaction_state = models.CharField(max_length=50)
    reference = models.CharField(max_length=100, unique=True)
    response = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    response_code = models.CharField(max_length=10)
    notification_response = models.TextField()
    record = models.TextField()

    def  __str__(self):
        return self.name

class Department(GenericBaseModel):
    pass

class Roles(GenericBaseModel):
    pass

class Permissions(GenericBaseModel):
    pass

class State(GenericBaseModel):
    pass

class RolePermissions(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="role_permissions")
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name="role_permissions")
    permissions = models.ForeignKey(Permissions, on_delete=models.CASCADE, related_name="role_permissions")
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="role_permissions")

    def __str__(self):
        return f"{self.role.name} - {self.permissions.name}"

class Representative(GenericBaseModel):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name="representatives")
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

class Organisation(GenericBaseModel):
    is_approved = models.BooleanField(default=False)
    business_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    registration_no = models.CharField(max_length=100, unique=True)
    tax_id = models.CharField(max_length=30, unique=True)
    incorporation_date = models.DateField()
    legal_status = models.CharField(max_length=50)
    industry_sector = models.CharField(max_length=50)
    physical_address = models.TextField()
    mailing_address = models.TextField()
    phone_no = models.CharField(max_length=20)
    website_url = models.URLField(blank=True, null=True)
    org_rep = models.ForeignKey(Representative, on_delete=models.CASCADE, related_name="organisations")
    incorporation_cert = models.FileField(upload_to="media/orgDocs/IncorporationCerts/")
    tax_exemption_cert = models.FileField(upload_to="media/orgDocs/TaxExemptionCerts/")
    proof_of_address = models.FileField(upload_to="media/orgDocs/ProofOfAddress/")
    list_of_directors = models.FileField(upload_to="media/orgDocs/ListOfDirectors/")
    organisational_chart = models.FileField(upload_to="media/orgDocs/OrganisationalChart/")
    recent_financial_statements = models.FileField(upload_to="media/orgDocs/RecentFinancialStatements/")
    auth_letter_of_rep = models.FileField(upload_to="media/orgDocs/AuthLetter/")
    logo = models.FileField(upload_to="media/orgDocs/logo/")

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    role = models.ForeignKey(RolePermissions, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    profile_pic = models.FileField(upload_to="media/profile/profilePics", blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

class UserSession(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sessions")
    otp = models.CharField(max_length=10)
    otp_created_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def expire_otp(self):
        self.is_valid = False
        self.save()

    def is_otp_expired(self):
        return timezone.now() - self.otp_created_at > timezone.timedelta(hours=8)

class ForgotPassword(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="password_resets")
    otp = models.CharField(max_length=10)
    otp_created_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def expire_otp(self):
        self.is_valid = False
        self.save()

    def is_otp_expired(self):
        return timezone.now() - self.otp_created_at > timezone.timedelta(minutes=5)

class NotificationType(GenericBaseModel):
    """
    A simple model to distinguish between SMS and EMAIL notifications.
    """
    pass


class Template(models.Model):
    """
    A template for a notification message. In this example we store a dictionary of
    language-to-message mappings in a JSONField (available in Django 3.1+).
    This allows the service to retrieve a language-specific message using getattr().
    """
    code = models.CharField(max_length=50)
    corporate = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    translations = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __getattr__(self, item):
        """
        Allow dynamic attribute access to language strings.
        For example, if a Template instance has translations = {"en": "Hello"},
        then getattr(template, 'en') will return "Hello".
        """
        # Note: This is only called if the attribute is not found by the normal mechanism.
        if isinstance(self.translations, dict) and item in self.translations:
            return self.translations.get(item, '')
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")

    def __str__(self):
        return f"{self.code} for {self.corporate}"


class Notification(models.Model):
    """
    A record of a sent (or attempted) notification.
    """
    corporate = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    destination = models.CharField(max_length=255)
    message = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} to {self.destination}"

