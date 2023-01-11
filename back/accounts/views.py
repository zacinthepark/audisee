from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_list_or_404
from .models import User
from .serializers import UserListSerializer

# Create your views here.
@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = get_list_or_404(User)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
