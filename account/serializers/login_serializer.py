from rest_framework import serializers

from account.models import User


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "token")

        read_only_fields = ["token"]
