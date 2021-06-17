from django.urls import path, re_path,include
from rest_framework import renderers,routers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

work_list=views.WorkViewSet.as_view({
     'get':'list',
     'post':'create',
})

work_detail =views.WorkViewSet.as_view({
    'post':'update',
    'patch':'partial_update',
    'delete':'destroy',
})


user_list=views.UserViewSet.as_view({
     'post':'create',
})

user_detail=views.UserViewSet.as_view({
     'get':'retrieve',
})



router =routers.DefaultRouter()



urlpatterns=[
     path('create/', views.UserCreate.as_view()),
     path('detail/',user_detail,name='user-detail'),
     path('work/',work_list,name='work-list'),
     path('work/<str:pk>/',work_detail,name='work-detail'),
    
]

urlpatterns=format_suffix_patterns(urlpatterns)