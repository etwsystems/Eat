from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from eatapp.serializers import UserSerializer, GroupSerializer, MenusSerializer, ResSerializer, CatSerializer, ResPostSerializer, CustomerSerializer
from eatapp.models import Menus, Restaurants, Categories, Orders, Customer
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
# from .forms import BookingForm, RoomForm, DateForm, RoomtypeForm
from datetime import datetime
from django.shortcuts import get_object_or_404
import random, requests, json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication as OriginalSessionAuthentication

class SessionAuthentication(OriginalSessionAuthentication):
    def enforce_csrf(self, request):
        return


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MenusViewSet(viewsets.ModelViewSet):
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer

class ResViewSet(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = ResSerializer    

class CatViewSet(viewsets.ModelViewSet):
	queryset= Categories.objects.all()
	serializer_class = CatSerializer

class MenusViewSetRes(viewsets.ModelViewSet):
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('categoriesno','resno')
	queryset= Menus.objects.all()
	serializer_class = MenusSerializer

# def datas(request):

class restpos(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = ResPostSerializer

class Customerviewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer




@api_view(['POST'])
def restpost(request):
    # if request.method == 'GET':
    #     serializer = ResPostSerializer
    #     return Response(serializer.data)
    # authentication_classes = (SessionAuthentication)
    if request.method == 'POST':
        serializer = ResPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            test = request.data['resno']
            test3 = Restaurants.objects.get(resno=1).rescode
            test2 = test
            # values = request.data
            values = {'rescode': test3}
            print(test3)

            headers =  {'content-type': 'application/json'}
            r=requests.post('http://localhost:3100/', data=json.dumps(values), headers=headers)
            t=r.text
            # print(r.text)

            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def detail(request):
    if request.method == "POST":
        values={'test':'test'}
        headers =  {'content-type': 'application/json'}
        r=requests.post('http://localhost:3100/', data=json.dumps(values), headers=headers)
        t=r.text
        print(r.text)
        return HttpResponse(t)

    template = loader.get_template('eatapp/index.html')
   
    return HttpResponse(template.render(request))		



# @csrf_exempt
# def rng(request):
# 	if request.method =="GET":

# 		a = 

# 	return HttpResponse(x)
