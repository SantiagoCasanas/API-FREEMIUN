from django.contrib import admin
from .models import PlanSubscription, Subscription

# Register your models here.
admin.site.register(PlanSubscription)
admin.site.register(Subscription)