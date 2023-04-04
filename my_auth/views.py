from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions

from .serializers import *


class AuthUserAPIView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            res = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(res, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):

    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            login(request, user)

            refresh = RefreshToken.for_user(user)
            global ACCESS_TOKEN_GLOBAL
            ACCESS_TOKEN_GLOBAL = str(refresh.access_token)
            serializer = self.serializer_class(user)

            response = Response()
            response.set_cookie('Access_Token', str(refresh.access_token))  # Bearer??
            response.set_cookie('logged_in', True)
            response.set_cookie(key='jwt', value=ACCESS_TOKEN_GLOBAL, httponly=True)
            response.data = serializer.data

            return Response({'Token': ACCESS_TOKEN_GLOBAL, **serializer.data}, status=status.HTTP_200_OK)

        return Response({'message': "Invalid credentials, try again!"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        response = Response()
        response.delete_cookie('jwt')
        logout(request)
        response.data = {
            'message': 'Successfully logged out!'
        }
        return response
