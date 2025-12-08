from django.db import models
from django.contrib.auth.models import User

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_clicks = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)
    click_value = models.IntegerField(default=1)
    auto_click_rate = models.IntegerField(default=0)
    last_tick = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s profile"