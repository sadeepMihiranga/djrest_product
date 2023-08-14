from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
