from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_event_date_not_future(date):
    current_date = timezone.now()
    if date > current_date:
        raise ValidationError('Event date can not be in the future')
    return date