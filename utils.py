from tradingsystem.settings import SECRET_KEY
import jwt

from django.http import JsonResponse

# from tradingsystem.settings import SECRET_KEY, ALGORITHM
from user.models import User

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        if not request.header.get('Authorization'):
            return JsonResponse({'message':'NO_TOKEN'}, status=403)
        token = request.headers['Authorization']

        try: 
            # decoded_token = jwt.decode(token, SECRET_KEY, ALGORITHM)
            # request.user = User.objects.get(id = decoded_token['user_id'])
            print(1)
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status=403)
        
        return func(self, request, *args, **kwargs)
    
    return wrapper
