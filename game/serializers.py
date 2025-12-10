from rest_framework import serializers
from .models import PlayerProfile

class PlayerProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = PlayerProfile
        fields = [
            "username",
            "total_clicks",
            "gold",
            "click_value",
            "auto_click_rate",
        ]