# encoding:utf-8
import json

from django.conf.urls import url
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from tastypie import http
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash

from ..models import Profile

class AuthResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowd_methods = ['post', 'put']
        resource_name = 'auth'
        serializer = Serializer(formats=['json'])

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/register%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('register'), name="register"),
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login'), name="login"),
        ]

    def register(self,request, **kwargs):
        json_data = json.loads(request.body)
        username = json_data['username']
        password = json_data['password']
        email = json_data['email']

        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            return self.create_response(request,
                                        data={"error":"用户名或邮箱已存在"},
                                        response_class=http.HttpBadRequest)

        user = User.objects.create_user(username,email=email,password=password)
        return self.create_response(request,
                                    data={
                                        "id": user.id,
                                        "username": user.username
                                    })


    def login(self, request, **kwargs):
        json_data = json.loads(request.body)
        username = json_data['username']
        password = json_data['password']

        user = authenticate(username=username,password=password)
        if user is None:
            return  self.create_response(request,data={"error":"错误的用户名或密码"},
                                         response_class=http.HttpUnauthorized)

        login(request, user)
        return self.create_response(request,
                                    data={
                                        "id": user.id,
                                        "username": user.username
                                    },response_class=http.HttpUnauthorized)


class ProfileResource(ModelResource):
    class Meta:
        queryset = Profile.objects.all()
        allowd_methods = ['post', 'put']
        resource_name = 'user'
        serializer = Serializer(formats=['json'])