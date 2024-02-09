from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Administrator
from .serializers import AdministratorSerializer
from rest_framework import generics
from rest_framework.response import Response
from .middleware import CustomMiddleware


class AdminListView(generics.ListCreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer

    def post(self, request, *args, **kwargs):
        payload = request.data
        print("payload-data:", payload)
        serializer = self.get_serializer(data=payload, context={'request': request})
        print("serializer data:", serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer

    # custom middleware code
    # def perform_create(self, serializer):
    #     current_user = CustomMiddleware().get_current_user()
    #     serializer.save(username=current_user.username)


class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
