import uuid

from django.db import models


STATUS_CHOICES = (
    ('PE', 'Pending'),
    ('CO', 'Completed'),
    ('CA', 'Canceled')
)


class UUIDableBehaviour(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimestampableBehaviour(models.Model):

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-create_date']


class StatustableBehaviour(models.Model):

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PE')

    class Meta:
        abstract = True

    def status_display(self):
        return self.get_status_display()