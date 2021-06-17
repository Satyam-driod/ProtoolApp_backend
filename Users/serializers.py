from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import render ,get_object_or_404,get_list_or_404
from .models import Work

class UserSerializer(serializers.ModelSerializer):
    # work=serializers.HyperlinkedRelatedField(many=True,view_name="work_list",read_only=True)
    confirm_password=serializers.CharField(min_length=8,max_length=100,write_only=True,required=True)

    class Meta:
        model=User
        fields = ['id','email','username','password','confirm_password','is_staff']
        extra_kwargs={'password':{'write_only':True},'is_staff': {'read_only': False}}

    def create(self,validate_data):
        user=User.objects.create_user(
            username=validate_data['username'],
            email=validate_data['email'],
            password=validate_data['password']
        )
        Token.objects.create(user=user)
        return user

    def validate(self,data):
        if(data.get('password')!=data.get('confirm_password')):
            raise serializers.ValidationErro8wr({"password":"Passwords don't match"})
        return data



class WorkSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    user_id=serializers.PrimaryKeyRelatedField(
    write_only=True,
    source="user",
    queryset=User.objects.all(),
    )
    class Meta:
        model=Work
        fields="__all__"