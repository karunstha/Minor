from django.shortcuts import render
from rest_framework.views import APIView
from restaurant.serializers import RestaurantSerializer,MenuSerializer
from rest_framework.response import Response
from restaurant.models import Menu,Restaurant
# Create your views here.
class RestaurantView(APIView):
    res_serializer = RestaurantSerializer
    def post(self,request):
        serializer = self.res_serializer(data = request.data)
        if(serializer.is_valid()):
            # print("Serializer is " + serializer)
            obj = serializer.save()

            print("Current Object is + " + str(obj))
            new_menu = Menu(restaurant=obj)
            new_menu.save()
            return Response('New Restaurant has been Saved')
        else:
            return Response(serializer.error_messages)

