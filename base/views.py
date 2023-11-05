from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
     class Meta:
        model = Product
        fields = '__all__'



# Create your views here.
@api_view(['get'])
def index(req):
    return Response ("test")


@api_view(['get'])
@permission_classes([IsAuthenticated])
def about(req):
    return Response("secret")

@api_view(['get'])
def products(req):
    prod = Product.objects.all()
    prod_ser = ProductSerializer(prod, many = True)
    return Response(prod_ser.data)



@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password']
            )
    
    user.save()
    return Response("new user born")