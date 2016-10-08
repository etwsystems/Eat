from django.contrib.auth.models import User, Group
from rest_framework import serializers
from eatapp.models import Menus, Restaurants, Categories, Orders, OrderDetails, Customer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ResSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        # fields = ('resno', 'name')        

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        # fields = ('itemname', 'itemdescription', 'itemno')

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories

class ResPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer