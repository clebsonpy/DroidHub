from django.conf import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.password_validation import (
    validate_password,
    get_password_validators
)
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers, exceptions
from django.core.exceptions import ValidationError

from demands.models import Address
from .models import User, Profile


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)
        token['username'] = user.username
        token['name'] = None
        token['email'] = user.email
        if hasattr(user, 'profile'):
            token['cpf_cnpj'] = user.profile.cpf_cnpj
            token['phone'] = user.profile.phone
            token['address'] = user.profile.address.__str__()

        return token


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        exclude = ['id']


class ProfileSerializer(serializers.ModelSerializer):

    address = AddressSerializer(read_only=True)

    class Meta:
        model = Profile
        exclude = ['user']


class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']


class RegisterSerializer(WritableNestedModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    email = serializers.CharField(write_only=True)

    address = AddressSerializer(many=False, required=True)

    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

    def is_unique(self, model, **kwargs):
        try:
            model.objects.get(**kwargs)
            return False
        except model.DoesNotExist:
            return True

    def validate(self, data):

        username = data.pop('username')
        password = data.pop('password')
        password_confirm = data.pop('password_confirm')
        email = data.pop('email')
        cpf_cnpj = data.get('cpf_cnpj')

        errors = {}

        if not self.is_unique(User, username=username):
            errors['username'] = _("Username already taken")

        if not self.is_unique(User, email=email):
            errors['email'] = _("E-mail already taken")

        if not self.is_unique(Profile, cpf_cnpj=cpf_cnpj):
            errors['cpf_cnpj'] = _("CPF/CNPJ must be unique")

        if password != password_confirm:
            errors['password'] = _("Confirmation password did not match")
        else:
            try:
                validate_password(
                    password,
                    password_validators=get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
                )
            except ValidationError as e:
                errors['password'] = e.messages

        if errors:
            raise exceptions.ValidationError(errors)

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        data['user'] = user

        return data
