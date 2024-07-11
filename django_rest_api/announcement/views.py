from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from .utils import send_code_to_user


class RegisterUserView(GenericAPIView):
	serializer_class = UserRegisterSerializer

	def post(self, request):
		user_data = request.data
		serializer = self.serializer_class(data=user_data)
		if seriliazer.is_valid(raise_exception=True):
			serializer.save()
			user = serializer.user_data
			send_code_to_user(user['email'])
			# send email function user['email']
			return Response({
				'data': user,
				'message': f"Hi, thanks for signing up a passcode has been sent to your email address"
			}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
