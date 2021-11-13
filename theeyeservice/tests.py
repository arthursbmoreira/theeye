from django.core.exceptions import ValidationError
from django.test import TestCase
from theeyeservice.models import Event, Payload, Form
from datetime import datetime

class EventTestCase(TestCase):
    def setUp(self):
        date = datetime.fromisoformat('2021-01-01 09:15:27.243860')

        pageview_event = Event.objects.create(session_id='e2085be5-9137-4e4e-80b5-f1ffddc25423', category='page interaction', name='pageview', timestamp=date)
        Payload.objects.create(host='www.consumeraffairs.com', path='/', event=pageview_event)
        
        click_event = Event.objects.create(session_id='e2085be5-9137-4e4e-80b5-f1ffddc25423', category='page interaction', name='cta_click', timestamp=date)
        Payload.objects.create(host='www.consumeraffairs.com', path='/', element='chat bubble', event=click_event)
        
        form_event = Event.objects.create(session_id='e2085be5-9137-4e4e-80b5-f1ffddc25423', category='form interaction', name='submit', timestamp=date)
        form_payload = Payload.objects.create(host='www.consumeraffairs.com', path='/', event=form_event)
        Form.objects.create(first_name='John', last_name='Doe', payload=form_payload)



    def test_events_created(self):
        pageview_event = Event.objects.get(name='pageview')
        click_event = Event.objects.get(name='cta_click')
        form_event = Event.objects.get(name='submit')
        
        self.assertEqual(pageview_event.session_id, 'e2085be5-9137-4e4e-80b5-f1ffddc25423')
        self.assertEqual(click_event.session_id, 'e2085be5-9137-4e4e-80b5-f1ffddc25423')
        self.assertEqual(form_event.session_id, 'e2085be5-9137-4e4e-80b5-f1ffddc25423')

    def test_event_in_future(self):
        future_date = datetime.fromisoformat('3021-01-01 09:15:27.243860')
        future_event = Event(session_id='e2085be5-9137-4e4e-80b5-f1ffddc25424', category='page interaction', name='pageview', timestamp=future_date)
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

    