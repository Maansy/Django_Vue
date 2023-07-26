# to take data from database and makes it presentable for the frontend

from rest_framework import serializers
from .models import Lead
from django.contrib.auth.models import User


class LeasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lead
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at'
        )
        fields = (
            'id',
            'company',
            'contact',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'created_at',
            'modified_at'
        )
