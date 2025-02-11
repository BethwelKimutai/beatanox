from django.urls import path, include

from Authentication.views import login, create_organization, create_department, create_role, create_permissions, \
    create_state, approve_organization, create_notification_type

urlpatterns = [
    path("login/", login, name= "login"),
    path("org_creation/", create_organization, name= "org-creation"),
    path("org_approval/", approve_organization, name="org-approval"),
    path("dept_creation/", create_department, name="dept-creation"),
    path("role_creation/", create_role, name="role-creation"),
    path("permission_creation/", create_permissions, name="permissions-creation"),
    path("state_creation/", create_state, name="state-creation"),
    path("notification_type_creation/", create_notification_type, name="notification-type-creation"),
]
