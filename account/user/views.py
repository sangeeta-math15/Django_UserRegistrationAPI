from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import FieldDoesNotExist, ValidationError
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Register
import json


def user_register(request):
    """
     This method register user by using inbuilt User Models.
    Using create_user method, storing details into database.
    Returns response whether user registered or not.
    """
    if request.method == 'POST':
        try:
            # print(data)
            data = json.loads(request.body)
            user = User.objects.create_user(username=data.get('username'),
                                            password=data.get('password'),
                                            first_name=data.get('first_name'),
                                            last_name=data.get('last_name'))
            data = {'message':'new user registered successfully..'}
            return JsonResponse(data)
        except IntegrityError:
            exception = {'Exception':'already exists...!'}
            return JsonResponse(exception)
        except Exception as e:
            exc = {'Exception':str(e)}


def user_login(request):
    """
   This method logins registration based on username and password by using authenticate method.
    Returns response login is success or failed...
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = authenticate(username = data.get('username'),
                                password = data.get('password'))
            if user is not None:
                data = {'message':'successfully logged in..!'}
                return JsonResponse(data)
        except ValidationError:
            exc_value = {'Exception':'Values does not exists'}
            return JsonResponse(exc_value)






