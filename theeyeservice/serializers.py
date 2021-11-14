from rest_framework import serializers
from theeyeservice.models import Event, Payload, Form
from collections import OrderedDict
import logging

logger = logging.getLogger(__name__)

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['first_name', 'last_name']

    def to_representation(self, instance):
        logger.info('Removing empty values from Form representation')
        result = super(FormSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key]])

class PayloadSerializer(serializers.ModelSerializer):
    form = FormSerializer(many=False, required=False, allow_null=True)

    class Meta:
        model = Payload
        fields = ['host', 'path', 'element', 'form']

    def to_representation(self, instance):
        logger.info('Removing empty values from Payload representation')
        result = super(PayloadSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key]])

class EventSerializer(serializers.ModelSerializer):
    data = PayloadSerializer(many=False)

    class Meta:
        model = Event
        fields = ['session_id', 'category', 'name', 'timestamp', 'data']

    def create(self, validated_data):
        logger.info('Saving events - start')

        form = Form.objects.create(**validated_data.get('data').pop('form')) if 'form' in validated_data.get('data') else None
        data = validated_data.pop('data')
        data = Payload.objects.create(**data, form=form)
        event = Event.objects.create(**validated_data, data=data)
        
        logger.info('Saving events - end')
        return event