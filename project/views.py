from rest_auth.views import LogoutView
from rest_framework import permissions

from project_api import serializers
from rest_framework import mixins, viewsets

class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated)

