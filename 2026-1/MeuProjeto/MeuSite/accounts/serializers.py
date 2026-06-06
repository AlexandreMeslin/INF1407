from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class ChangePasswordSerializer(serializers.Serializer):
    '''
    Serializer for password change endpoint.
    '''
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        '''
        Validate the new password using Django's built-in validators.
        '''
        validate_password(value)
        return value

class ResetPasswordRequestSerializer(serializers.Serializer):
    '''
    Serializer for requesting a password reset.
    '''
    email = serializers.EmailField(required=True)

class ResetPasswordConfirmSerializer(serializers.Serializer):
    '''
    Serializer for confirming a password reset.
    '''
    code = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=8)

    def validate_new_password(self, value):
        '''
        Validate the new password using Django's built-in validators.
        '''
        validate_password(value)
        return value