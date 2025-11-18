from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from rest_framework import viewsets
from .models import Run
from .serializers import RunSerializer, UserSerializer
from django.contrib.auth.models import User


@api_view(["GET"])
def company_details(request):
    details = {
        "company_name": settings.COMPANY_NAME,
        "slogan": settings.SLOGAN,
        "contacts": settings.CONTACTS,
    }
    return Response(details)


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        filter_type = self.request.query_params.get('type')
        if filter_type == 'coach':
            return User.objects.filter(is_staff=True)
        if filter_type == 'athlete':
            return User.objects.filter(is_staff=False)
        if filter_type == None:
            return User.objects.all()

