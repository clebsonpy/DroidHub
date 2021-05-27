from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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
