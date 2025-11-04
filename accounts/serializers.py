from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from .models import Profile
User = get_user_model()

# User registraion serializer...
class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','password','confirm_password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    # validate all field data..
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('Two password do not match')
        
        return attrs
    
    # validation for password
    def validate_password(self,value):
        validate_password(value)
        return value
    
    # create user here 
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)

        return user


# Login Serializer 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password =serializers.CharField()


# password change serializer 
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    # validate new password 
    def validate_new_password(self,value):
        validate_password(value)
        return value


# user profile serializer..
class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)
    email = serializers.CharField(source='user.email',read_only=True)
    class Meta:
        model = Profile
        fields = ['id','username','email','phone','address']