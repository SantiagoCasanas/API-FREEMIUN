from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Subscription, PlanSubscription
from .serializers import SubscriptionSerializer, PlanSubscriptionSerializer


class PlanDetailView(APIView):
    Subscription.inactivar_sub_actuales
    Subscription.activar_nuevas_sub()
    def get(self, request, pk):
        plan = get_object_or_404(PlanSubscription, pk=pk)
        serializer = PlanSubscriptionSerializer(plan)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        plan = get_object_or_404(PlanSubscription, pk=pk)
        serializer = PlanSubscriptionSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SubscriptionListCreateView(APIView):
    Subscription.inactivar_sub_actuales
    Subscription.activar_nuevas_sub()
    def get(self, request):
        Subscription.inactivar_sub_actuales
        Subscription.activar_nuevas_sub()
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionDetailView(APIView):
    Subscription.inactivar_sub_actuales
    Subscription.activar_nuevas_sub()
    def get(self, request, pk):
        subscription = get_object_or_404(Subscription, pk=pk)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        subscription = get_object_or_404(Subscription, pk=pk)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCurrentSubscription(APIView):
    def get(self, request, pk):
        subscription = Subscription.obtener_sub_actual(pk)
        if subscription is None:
            return Response({'Freemiun': 'This is a freemiun user.'},
                            status=status.HTTP_200_OK)
        else:
           serializer = SubscriptionSerializer(subscription)
           return Response(serializer.data, status=status.HTTP_200_OK)