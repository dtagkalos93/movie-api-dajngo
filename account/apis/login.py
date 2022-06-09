from django.contrib.auth import authenticate
from rest_framework import response, status
from rest_framework.generics import GenericAPIView

from account.serializers.login_serializer import LoginSerializer


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            return response.Response(
                {"message": "Invalid Credentials. Try again."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        serializer = self.serializer_class(user)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
