from django.utils.timezone import now

from Authentication.models import TransactionType
from registry.logbase import TransactionLogBase
from registry.responseprovider import ResponseProvider


def log_login_transaction(request, user):
    transaction_log = TransactionLogBase()

    # Ensure "Login" Transaction Type Exists
    transaction_type_data = transaction_log.registry.database('transactiontype', 'get', data={"name": "Login"})

    if not transaction_type_data:  # If "Login" type does not exist, create it
        transaction_type_data = transaction_log.registry.database('transactiontype', 'create',
                                                                  data={"name": "Login",
                                                                        "description": "User Login Transaction"})

    # Convert the dictionary to an actual TransactionType model instance
    transaction_type_instance = TransactionType.objects.get(id=transaction_type_data['id'])

    # Log the Login Transaction
    transaction_log.log_transaction(
        transaction_type=transaction_type_instance,  # Pass the model instance, not a dictionary
        request=request,
        source_ip=request.META.get("REMOTE_ADDR"),
        transaction_state="Completed",
        reference=f"LOGIN-{user.id}-{now().timestamp()}",
        response="200.000.000",
        amount=0.00,
        response_code="200",
        notification_response="N/A",
        record="User login successful",
        euser=user
    )

    response_provider = ResponseProvider(message="Transaction logged successfully", code=200)
    return response_provider.success()