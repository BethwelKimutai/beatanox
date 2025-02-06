from django.db.models import QuerySet
from .ServiceBase import ServiceBase
from Authentication.models import (
    Organisation, User, RolePermissions, UserSession, ForgotPassword, Representative,
    Department, Permissions, Roles, State
)


class OrganisationService(ServiceBase):
    def __init__(self):
        super().__init__(Organisation.objects)


class UserService(ServiceBase):
    def __init__(self):
        super().__init__(User.objects)


class RolePermissionService(ServiceBase):
    def __init__(self):
        super().__init__(RolePermissions.objects)


class SessionService(ServiceBase):
    def __init__(self):
        super().__init__(UserSession.objects)

    def validate_otp(self, user, otp):
        session = self.get(user=user, otp=otp, is_valid=True)
        if session and not session.is_otp_expired():
            session.expire_otp()
            return True
        return False


class ForgotPasswordService(ServiceBase):
    def __init__(self):
        super().__init__(ForgotPassword.objects)

    def validate_otp(self, user, otp):
        reset_request = self.get(user=user, otp=otp, is_valid=True)
        if reset_request and not reset_request.is_otp_expired():
            reset_request.expire_otp()
            return True
        return False


class RepresentativeService(ServiceBase):
    def __init__(self):
        super().__init__(Representative.objects)


class DepartmentService(ServiceBase):
    def __init__(self):
        super().__init__(Department.objects)


class PermissionsService(ServiceBase):
    def __init__(self):
        super().__init__(Permissions.objects)


class RoleService(ServiceBase):
    def __init__(self):
        super().__init__(Roles.objects)


class StateService(ServiceBase):
    def __init__(self):
        super().__init__(State.objects)
