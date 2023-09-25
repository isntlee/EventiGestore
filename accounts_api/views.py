from rest_framework import status, viewsets
from rest_framework.response import Response
from accounts.models import User
from django.contrib.auth import authenticate, login
from .serializers import AccountSerializer


class AccountList(viewsets.ViewSet):
    serializer_class = AccountSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        account = authenticate(request, username=username, password=password)
        if account is not None:
            login(request, account)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
