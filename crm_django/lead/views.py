from django.shortcuts import render
from rest_framework import viewsets
from .models import Lead
from .serializers import LeasSerializers
# Create your views here.
# for showing on making it possible to get this serializers from the frontend

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeasSerializers
    queryset = Lead.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)