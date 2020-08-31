from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from fooditem import serializers
from fooditem.models import FoodItem
# Create your views here.
class FoodItemView(APIView):
    serializers_class = serializers.FoodItemSerializers

    def get(self,request,format = None):
        print(request.data)
        qs = FoodItem.objects.filter(name=request.data['name'])
        serializer = serializers.FoodItemSerializers(qs,many=True)
        food_item = {'food':serializer.data}
        return Response(food_item)

    def post(self,request):
        serializer = self.serializers_class(data=request.data)

        if(serializer.is_valid()):
            serializer.save()
            name = serializer.validated_data.get('name')
            return Response({'Item has been added':name})
        else:
            return Response(serializer.error_messages)
    
    def delete(self,request,pk):
        food_item = get_object_or_404(FoodItem.objects.all(),pk=pk)
        food_item.delete()
        return Response({"message": "FoodItem with id `{}` has been deleted.".format(pk)},status=204)