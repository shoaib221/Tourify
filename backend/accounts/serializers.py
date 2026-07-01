

from rest_framework import serializers
from residence.models import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password





class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [ 'name', 'id' ]
    
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


##################################################################



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = [ 'mail', 'mobile', 'nid', 'country', 'password' ]


class LoginSerializer(serializers.Serializer):
    mail = serializers.CharField( required=True )
    password = serializers.CharField( required=True )


class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = [ 'mail', 'mobile', 'nid', 'country' ]


class UserSerializer( serializers.ModelSerializer ):

    class Meta:
        model = User
        fields = [ 'username', 'password' ]



class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["email"],
            email=validated_data["email"],
            password=make_password(validated_data["password"])
        )
        return user