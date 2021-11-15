from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from theeyeservice.models import Event, Payload, Form
from datetime import datetime

class EventTestCase(TestCase):
    def setUp(self):
        date = datetime.fromisoformat('2021-01-01 09:15:27.243860')

        payload1 = Payload.objects.create(host='www.consumeraffairs.com', path='/')
        Event.objects.create(session_id='e2085be5-9137-4e4e-80b5-f1ffddc25423', category='page interaction', name='pageview', timestamp=date, data=payload1)
        
        payload2 = Payload.objects.create(host='www.consumeraffairs.com', path='/', element='chat bubble')
        Event.objects.create(session_id='e2085be5-9137-4e4e-80b5-f1ffddc25423', category='page interaction', name='cta_click', timestamp=date, data=payload2)
        
        form = Form.objects.create(first_name='John', last_name='Doe')
        payload3 = Payload.objects.create(host='www.consumeraffairs.com', path='/', form=form)
        Event.objects.create(session_id='e2085be5-9137-4e4e-80b5-f1ffddc25423', category='form interaction', name='submit', timestamp=date, data=payload3)

    def test_events_created(self):
        pageview_event = Event.objects.get(name='pageview')
        click_event = Event.objects.get(name='cta_click')
        form_event = Event.objects.get(name='submit')
        
        self.assertEqual(pageview_event.session_id, 'e2085be5-9137-4e4e-80b5-f1ffddc25423')
        self.assertEqual(click_event.session_id, 'e2085be5-9137-4e4e-80b5-f1ffddc25423')
        self.assertEqual(form_event.session_id, 'e2085be5-9137-4e4e-80b5-f1ffddc25423')

    def test_event_in_future(self):
        current_date = timezone.now()
        future_date = current_date.replace(current_date.year + 100)
        payload = Payload.objects.create(host='www.consumeraffairs.com', path='/')
        future_event = Event(session_id='e2085be5-9137-4e4e-80b5-f1ffddc25424', category='page interaction', name='pageview', timestamp=future_date, data=payload)
        with self.assertRaises(ValidationError):
            future_event.full_clean()
        
    def test_payloads_created(self):
        pageview_event = Event.objects.get(name='pageview')
        click_event = Event.objects.get(name='cta_click')
                
        self.assertEqual(pageview_event.data.host, 'www.consumeraffairs.com')
        self.assertEqual(click_event.data.element, 'chat bubble')
        
    def test_form_in_payload(self):
        form_event = Event.objects.get(name='submit')
        self.assertEqual(form_event.data.form.first_name, 'John')

    