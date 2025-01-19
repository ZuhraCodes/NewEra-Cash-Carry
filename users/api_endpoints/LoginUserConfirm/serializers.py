from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .utils import get_tokens_for_users
from datetime import datetime, timedelta
from django.core.cache import cache

User = get_user_model()


class NewLoginConfirmSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(
        regex=r'^\+998\d{9}$',
        error_messages = {
            'invalid': 'Phone number must be in the format +998xxxxxxxxx.'
        }
    )

    code = serializers.CharField()

    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        one_time_code = validated_data['code']

        cache_key = f"otp_{phone_number}"
        cache_otp_data = cache.get(cache_key)

        if not cache_otp_data:
            raise ValidationError({
                "error": "access_restricted",
                "message": "The OTP code is expired"
            })
        
        if str(cache_otp_data) != one_time_code:
            raise ValidationError({
                "error": "invalid_code",
                "message": "The OTP code is invalid"
            })
        
        user, created = User.objects.get_or_create(
            phone_number=phone_number, defaults={"username": phone_number}
        )
        tokens = get_tokens_for_users(user)

        return {
            "message": "You have logined successfully",
            "tokens": tokens
        }
