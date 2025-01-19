from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.cache import cache
import random
from datetime import datetime, timedelta

User = get_user_model()

class NewLoginSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(
        regex=r'^\+998\d{9}$',
        error_messages = {
            'invalid': 'Phone number must be in the format +9989xxxxxxxx.'
        }
    )

    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        one_time_code = random.randint(100000, 999999)

        print(one_time_code)
        cache_key = f"otp_{phone_number}"
        cache_otp_data = cache.get(cache_key)

        if cache_otp_data:
            raise ValidationError({
                "error": "code_already_sent",
                "message": "We have already sent code. You can try again after 60s"
            })

        User.objects.get_or_create(phone_number=phone_number, username=phone_number)

        cache.set(cache_key, one_time_code, 60)

        return {"message": "OTP sent successfully"}
