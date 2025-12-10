from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PlayerProfile
from .serializers import PlayerProfileSerializer

def home(request):
    from django.http import HttpResponse
    return HttpResponse("Clicker backend is alive!")

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = request.user.playerprofile
        serializer = PlayerProfileSerializer(profile)
        return Response(serializer.data)
    
class ClickView(APIView):
    
    def post(self, request):
        profile = PlayerProfile.objects.first()
        profile.total_clicks += 1
        profile.gold += profile.click_value
        profile.save()

        return Response({
            "gold": profile.gold,
            "total_clicks": profile.total_clicks,
        })
