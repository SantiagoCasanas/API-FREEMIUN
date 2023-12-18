import datetime
from django.db import models

class PlanSubscription(models.Model):
    name = models.CharField(unique = True, max_length = 50, null = False)
    description = models.CharField(null = False, max_length = 250)
    price = models.DecimalField(null = False, max_digits = 6, decimal_places = 2)
    days = models.IntegerField(null = False)
    farms = models.IntegerField(null = False)
    parcels = models.IntegerField(null = False)
    discounts = models.BooleanField(null = False)

    def __str__(self) -> str:
        return self.name
    
    

class Subscription(models.Model):
    user_id = models.IntegerField(null = False, blank = False)
    plan_subscription = models.ForeignKey(PlanSubscription, on_delete = models.PROTECT)
    date_init = models.DateField(null = False)
    date_end = models.DateField(null = False)
    "Is active represents a sub that has been payed, but is not necesarily the current sub"
    is_active = models.BooleanField(null = False, default = True)
    is_current = models.BooleanField(null = False, default = True)
        
    def __str__(self) -> str:
        return str(self.user_id)
    
    @staticmethod
    def inactivar_sub_actuales():
        for sub in Subscription.objects.all():
            if sub.is_active and sub.is_current:
                if datetime.date.today() < sub.date_end:
                    sub.is_active = False
                    sub.is_current = False
                    sub.save()
    @staticmethod
    def activar_nuevas_sub():
        for sub in Subscription.objects.all():
            if sub.is_active and not sub.is_current:
                if sub.date_init <= datetime.date.today() <= sub.date_end:
                    sub.is_current = True
                    sub.save()
    
    @staticmethod
    def obtener_sub_actual(user_id):
        sub = Subscription.objects.filter(user_id=user_id, 
                                          is_active=True, 
                                          is_current=True).first()
        
        return sub