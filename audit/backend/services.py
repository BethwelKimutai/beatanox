from Authentication.models import Transaction, Template, NotificationType, Notification


class TransactionService:
    def update(self, id, **kwargs):
        """
        Update a Transaction record by its primary key with any given fields.
        """
        try:
            transaction = Transaction.objects.get(pk=id)
            for key, value in kwargs.items():
                setattr(transaction, key, value)
            transaction.save()
            return transaction
        except Transaction.DoesNotExist:
            # In production, you might log an error or raise an exception
            return None


class TemplateService:
    def filter(self, **kwargs):
        """
        Return a queryset of Template objects matching the filter criteria.
        For example, filtering by template code and corporate.
        """
        return Template.objects.filter(**kwargs)


class NotificationTypeService:
    def get(self, **kwargs):
        """
        Retrieve a NotificationType matching the given criteria (e.g., name="SMS").
        Returns the first match or None.
        """
        return NotificationType.objects.filter(**kwargs).first()


class NotificationService:
    def create(self, **kwargs):
        """
        Create a Notification record.
        Expected keyword arguments include:
          - corporate (Organisation instance)
          - title (str)
          - destination (str)
          - message (str)
          - state (State instance)
          - notification_type (NotificationType instance)
        """
        return Notification.objects.create(**kwargs)

    def update(self, pk, **kwargs):
        """
        Update an existing Notification record by its primary key.
        """
        try:
            notification = Notification.objects.get(pk=pk)
            for key, value in kwargs.items():
                setattr(notification, key, value)
            notification.save()
            return notification
        except Notification.DoesNotExist:
            return None