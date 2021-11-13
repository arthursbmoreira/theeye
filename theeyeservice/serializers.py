from rest_framework import serializers
from theeyeservice.models import Event, Payload, Form

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
        data = validated_data.pop('data')
        if 'form' in data:
            form = data.pop('form')
        else:
            form = {}

        event = Event.objects.create(**validated_data)
        payload = Payload.objects.create(event=event, **data)
        Form.objects.create(payload=payload, **form)

        return event