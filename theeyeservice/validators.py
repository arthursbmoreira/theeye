from django.core.exceptions import ValidationError
from datetime import datetime

def validate_event_date_not_future(date):
    current_date = datetime.now()
    if date > current_date:
        raise ValidationError('Event date can not be in the future')
    return date