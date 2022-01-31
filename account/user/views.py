from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDetailsSerializer
from .models import UserDetails


class Register(APIView):
    """
    This class register new user based on the details..
    """
    def post(self, request):
        try:
            serializer = UserDetailsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'Message': 'user registered successfully'}, status=status.HTTP_201_CREATED)

        except ValueError:
            return Response(ValueError, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError:
            return Response("Exception:Username already exists!")

        except Exception as e:
            return Response({'Exception': str(e)})


class Login(APIView):
    """
    This class create login api and validate user details
    :return response of login success or fail.
    """

    def post(self, request):
        try:
            user = authenticate(username=request.data.get('username'),
                                password=request.data.get('password'))
            if user is not None:
                return Response("login successful..",
                                status=status.HTTP_202_ACCEPTED)
            else:
                return Response("username and password is wrong..!")
        except AuthenticationFailed:
            return Response("Exception: Athentication failed..",
                            status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'Exception': str(e)})
