# Generated by Django 5.1.5 on 2025-02-05 10:09

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericBaseModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RolePermissions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('genericbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.genericbasemodel')),
            ],
            options={
                'abstract': False,
            },
            bases=('Authentication.genericbasemodel',),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('genericbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.genericbasemodel')),
                ('is_approved', models.BooleanField(default=False)),
                ('business_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('registration_no', models.CharField(max_length=100, unique=True)),
                ('tax_id', models.CharField(max_length=30, unique=True)),
                ('incorporation_date', models.DateField()),
                ('legal_status', models.CharField(max_length=50)),
                ('industry_sector', models.CharField(max_length=50)),
                ('physical_address', models.TextField()),
                ('mailing_address', models.TextField()),
                ('phone_no', models.CharField(max_length=20)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('incorporation_cert', models.FileField(upload_to='media/orgDocs/IncorporationCerts/')),
                ('tax_exemption_cert', models.FileField(upload_to='media/orgDocs/TaxExemptionCerts/')),
                ('proof_of_address', models.FileField(upload_to='media/orgDocs/ProofOfAddress/')),
                ('list_of_directors', models.FileField(upload_to='media/orgDocs/ListOfDirectors/')),
                ('organisational_chart', models.FileField(upload_to='media/orgDocs/OrganisationalChart/')),
                ('recent_financial_statements', models.FileField(upload_to='media/orgDocs/RecentFinancialStatements/')),
                ('auth_letter_of_rep', models.FileField(upload_to='media/orgDocs/AuthLetter/')),
                ('logo', models.FileField(upload_to='media/orgDocs/logo/')),
            ],
            options={
                'abstract': False,
            },
            bases=('Authentication.genericbasemodel',),
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('genericbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.genericbasemodel')),
            ],
            options={
                'abstract': False,
            },
            bases=('Authentication.genericbasemodel',),
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('genericbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.genericbasemodel')),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('Authentication.genericbasemodel',),
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('genericbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.genericbasemodel')),
            ],
            options={
                'abstract': False,
            },
            bases=('Authentication.genericbasemodel',),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('genericbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.genericbasemodel')),
            ],
            options={
                'abstract': False,
            },
            bases=('Authentication.genericbasemodel',),
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('genericbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.genericbasemodel')),
                ('simple_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('Authentication.genericbasemodel',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('zip', models.CharField(blank=True, max_length=10, null=True)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='media/profile/profilePics')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Authentication.rolepermissions')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Authentication.organisation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(max_length=10)),
                ('otp_created_at', models.DateTimeField(auto_now_add=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ForgotPassword',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(max_length=10)),
                ('otp_created_at', models.DateTimeField(auto_now_add=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_resets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='rolepermissions',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_permissions', to='Authentication.department'),
        ),
        migrations.AddField(
            model_name='rolepermissions',
            name='permissions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_permissions', to='Authentication.permissions'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='org_rep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organisations', to='Authentication.representative'),
        ),
        migrations.AddField(
            model_name='rolepermissions',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_permissions', to='Authentication.roles'),
        ),
        migrations.AddField(
            model_name='representative',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representatives', to='Authentication.roles'),
        ),
        migrations.AddField(
            model_name='rolepermissions',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_permissions', to='Authentication.state'),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('genericbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.genericbasemodel')),
                ('source_ip', models.GenericIPAddressField()),
                ('request', models.TextField()),
                ('transaction_state', models.CharField(max_length=50)),
                ('reference', models.CharField(max_length=100, unique=True)),
                ('response', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('response_code', models.CharField(max_length=10)),
                ('notification_response', models.TextField()),
                ('record', models.TextField()),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='Authentication.transactiontype')),
            ],
            options={
                'abstract': False,
            },
            bases=('Authentication.genericbasemodel',),
        ),
    ]
