from rest_framework import serializers
from theeyeservice.models import Event, Payload, Form
import logging

logger = logging.getLogger(__name__)

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['first_name', 'last_name']

class PayloadSerializer(serializers.ModelSerializer):
    form = FormSerializer(many=False, required=False, allow_null=True)

    class Meta:
        model = Payload
        fields = ['host', 'path', 'element', 'form']

class EventSerializer(serializers.ModelSerializer):
    data = PayloadSerializer(many=False)

    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'timestamp', 'data']

    def create(self, validated_data):
        """
        Overriding the create method for the event serializer to save the payload and check if there is a Form in the payload.
        Other scenarios are possible, but that is to be defined.
        """
        logger.info('Saving events - start')

        form = Form.objects.create(**validated_data.get('data').pop('form')) if 'form' in validated_data.get('data') else None
        data = validated_data.pop('data')
        data = Payload.objects.create(**data, form=form)
        event = Event.objects.create(**validated_data, data=data)
        
        logger.info('Saving events - end')
        return event