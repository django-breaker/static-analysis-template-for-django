
import arrow
from datetime import datetime

from django.utils.timezone import utc
from rest_framework import serializers


class CreateMockRequestSerializer(serializers.Serializer):
    timezone = serializers.CharField(write_only=True)
    timestamp = serializers.IntegerField(min_value=0, write_only=True)

    def validate(self, attr):
        # Validate timezone
        timezone = attr['timezone']
        try:
            arrow.now(timezone)
        except arrow.parser.ParserError:
            raise ValidationError(f'Invalid timezone: {timezone}')

        # Validate timestamp
        timestamp = attr['timestamp']
        try:
            datetime.utcfromtimestamp(int(timestamp) // 1000).astimezone(utc)
        except ValueError as err:
            raise ValidationError(f'Invalid timestamp: {err}')

        return attr


class TimeInfo(serializers.Serializer):
    timezone = serializers.CharField(write_only=True)
    timestamp = serializers.IntegerField(min_value=0, write_only=True)
    formatted_datetime = serializers.CharField(write_only=True)
