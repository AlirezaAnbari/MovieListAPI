from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError


class RegisterationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
          password = self.valiated_data['password']
          password2 = self.valiated_data['password2']
          
          if password != password2:
              raise ValidationError({'error': 'password1 must be equal to password2'})
          
          if User.objects.filter(email=self.validated_data['email']).exists():
              raise ValidationError({'error': 'email already exists'})