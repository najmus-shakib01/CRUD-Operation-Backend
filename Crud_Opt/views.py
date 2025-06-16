from .models import Plan
from .serializers import PlanSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class PlanListCreateAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None, *args, **kwargs):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PlanRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk, format=None, *args, **kwargs):
        return get_object_or_404(Plan, id=pk)
    
    def get(self, request, pk, format=None, *args, **kwargs):
        plans = self.get_object(pk)
        serializer = PlanSerializer(plans)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None, *args, **kwargs):
        plans = self.get_object(pk)
        serializer = PlanSerializer(plans, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None, *args, **kwargs):
        plans = self.get_object(pk)
        plans.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)