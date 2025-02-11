from api.utility.common import get_clean_data


def create_organisation_data(request):
    """
    Extract and map organisation data from the cleaned request data.

    This function assumes that the request payload contains all necessary fields
    to create an Organisation instance. Adjust the keys if your payload differs.
    """
    data = get_clean_data(request)

    organisation_data = {
        # Fields inherited from GenericBaseModel
        "name": data.get("name"),  # optional: add validation if required
        "description": data.get("description"),

        # Organisation-specific fields
        "is_approved": data.get("is_approved", False),
        "business_name": data["business_name"],
        "email": data["email"],
        "registration_no": data["registration_no"],
        "tax_id": data["tax_id"],
        "incorporation_date": data["incorporation_date"],  # ensure date format is correct
        "legal_status": data["legal_status"],
        "industry_sector": data["industry_sector"],
        "physical_address": data["physical_address"],
        "mailing_address": data["mailing_address"],
        "phone_no": data["phone_no"],
        "website_url": data.get("website_url"),  # optional field

        # ForeignKey: assuming the representative is provided as an ID or instance.
        "org_rep": data["org_rep"],

        # File fields – ensure you’re handling file uploads appropriately
        "incorporation_cert": data["incorporation_cert"],
        "tax_exemption_cert": data["tax_exemption_cert"],
        "proof_of_address": data["proof_of_address"],
        "list_of_directors": data["list_of_directors"],
        "organisational_chart": data["organisational_chart"],
        "recent_financial_statements": data["recent_financial_statements"],
        "auth_letter_of_rep": data["auth_letter_of_rep"],
        "logo": data["logo"],
    }

    return organisation_data

def create_user_data(request):
    data = get_clean_data(request)
    user_data = {
        "username": data["username"],
        "password": data["password"],
        "email": data["email"],
        "role": data["role"],
        "organization": data["organization_id"]
    }
    return user_data


def create_department_data(request):
    """
    Extracts and returns data for creating a Department instance.
    Expected keys in the cleaned data: 'name', 'description'
    """
    data = get_clean_data(request)
    department_data = {
        "name": data.get("name"),
        "description": data.get("description"),
    }
    return department_data

def create_roles_data(request):
    """
    Extracts and returns data for creating a Roles instance.
    Expected keys in the cleaned data: 'name', 'description'
    """
    data = get_clean_data(request)
    roles_data = {
        "name": data.get("name"),
        "description": data.get("description"),
    }
    return roles_data

def create_permissions_data(request):
    """
    Extracts and returns data for creating a Permissions instance.
    Expected keys in the cleaned data: 'name', 'description'
    """
    data = get_clean_data(request)
    permissions_data = {
        "name": data.get("name"),
        "description": data.get("description"),
    }
    return permissions_data

def create_state_data(request):
    """
    Extracts and returns data for creating a State instance.
    Expected keys in the cleaned data: 'name', 'description'
    """
    data = get_clean_data(request)
    state_data = {
        "name": data.get("name"),
        "description": data.get("description"),
    }
    return state_data


def create_rolepermissions_data(request):
    """
    Extracts and returns data for creating a RolePermissions instance.
    Expected keys in the cleaned data:
      - 'department'
      - 'role'
      - 'permissions'
      - 'state'

    The values for these keys should be valid identifiers or instances that
    can be used to resolve the respective ForeignKey relationships.
    """
    data = get_clean_data(request)
    rolepermissions_data = {
        "department": data["department"],
        "role": data["role"],
        "permissions": data["permissions"],
        "state": data["state"],
    }
    return rolepermissions_data


def create_representative_data(request):
    """
    Extracts and returns data for creating a Representative instance.
    Expected keys in the cleaned data:
      - 'name'
      - 'description'
      - 'role'
      - 'phone'
      - 'email'

    Ensure that the 'role' value is either a valid identifier or instance.
    """
    data = get_clean_data(request)
    representative_data = {
        "name": data.get("name"),
        "description": data.get("description"),
        "role": data["role"],
        "phone": data["phone"],
        "email": data["email"],
    }
    return representative_data
