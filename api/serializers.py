from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = user
        fields = ['url', 'username', 'email', 'groups']
        
 class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    
    class meta:
        model = Group
        fields = ['url', 'name']