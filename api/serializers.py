import datetime
from rest_framework import serializers
from .models import PlanSubscription, Subscription
from datetime import date, timedelta
from django.shortcuts import get_object_or_404

class PlanSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanSubscription
        fields = ['id', 'name', 'description', 'price', 'days', 'farms', 'parcels', 'discounts']

        extra_kwargs = {
                'id': {"required": True},
                "name":{"required" : True},
                "description":{"required" : True},
                "price":{"required" : True},
                "days":{"required" : True}
        }

        def create(self, validated_data):
            plan_sub = PlanSubscription(**validated_data)
            plan_sub.save()
        

class SubscriptionSerializer(serializers.ModelSerializer):
    plan_subscription_name = serializers.CharField(source='plan_subscription.name', read_only=True)
    """
    Serializer class for serializing and deserializing instances of the Subscription model.

    Fields:
    - id (int): The ID of the subscription.
    - user_id (int): The ID of the user associated with the subscription.
    - plan_subscription (int): The ID of the plan subscription associated with the subscription.
    - is_active (bool): Indicates if the subscription is active.
    - is_current (bool): Indicates if the subscription is the current one.
    """

    class Meta:
        model = Subscription
        fields = ['user_id', 'plan_subscription', 'plan_subscription_name', 'date_init', 'date_end', 'is_active', 'is_current']

        extra_kwargs = {
            "user_id": {"required": True},
            "plan_subscription": {"required": True},
            "date_init": {"required": False},
            "date_end": {"required": False},
        }

    def create(self, validated_data):
        """
        Create a new Subscription instance based on the validated data.

        Args:
            validated_data (dict): The validated data for creating the Subscription instance.

        Returns:
            Subscription: The created Subscription instance.
        """
        plan_sub_id = validated_data.get('plan_subscription')
        plan_sub = get_object_or_404(PlanSubscription, id=plan_sub_id.id)
        subscription = Subscription(**validated_data)

        
        current = Subscription.objects.filter(
            user_id=validated_data.get('user_id'),
            is_active=True,
            is_current=True
        ).first()
        if current is None:
            subscription.date_init = datetime.date.today()
            subscription.date_end = datetime.date.today() + timedelta(days=plan_sub.days)
        else:
            subscription.date_init = current.date_end
            subscription.date_end = current.date_end + timedelta(days=plan_sub.days)
            subscription.is_current = False
            if current.plan_subscription != plan_sub:
                current.plan_subscription = plan_sub
                current.save()
        subscription.save()

        return subscription