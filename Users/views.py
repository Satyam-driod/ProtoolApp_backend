from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, generics, authentication, permissions,response
from  rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import Work
from .serializers import UserSerializer,WorkSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.decorators import action


# Create your views here.w65vhg
class WorkViewSet(viewsets.ModelViewSet):
    queryset=Work.objects.all()
    serializer_class=WorkSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]   

    @action(detail=True,methods=['get'])
    def list(self,request,**kwargs):
        user=request.user
        work=Work.objects.filter(user=user)
        # print(work)
        serializer=self.serializer_class(work,many=True)
        return Response(serializer.data)

    # def create(self,serializer,**kwargs):
    #     serializer.save(user=self.request.user)


class UserCreate(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def retrieve(self,request,*args,**kwargs):
        return response.Response({
            'id':request.user.id,
            'username':request.user.username,
        })

class GetToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data,context={'request':request})

        serializer.is_valid(raise_exception=True)
        user =serializer.validated_data['user']
        token=Token.objects.get(user=user)

        return response.Response({
            'token':token.key,
        })





   


# Create your views here.

