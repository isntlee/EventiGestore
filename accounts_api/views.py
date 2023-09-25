from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login
from accounts.models import User
from .serializers import AccountSerializer


class AccountList(viewsets.ViewSet):
    serializer_class = AccountSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description'] 

    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        account = authenticate(request, username=username, password=password)
        if account is not None:
            login(request, account)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        queryset = User.objects.all()
        search_param = self.request.query_params.get('search')
        if search_param:
            queryset = queryset.filter(Q(description__icontains=search_param))
        return queryset

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, **kwargs):
        item = self.kwargs.get('pk')
        event = get_object_or_404(self.get_queryset(), slug=item)
        serializer = self.serializer_class(event)
        return Response(serializer.data)

    def update(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), slug=pk)
        serializer = AccountSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), slug=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)