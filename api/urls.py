from django.urls import path
from .views import SubscriptionListCreateView, SubscriptionDetailView, GetCurrentSubscription, PlanDetailView

urlpatterns = [
    path('plan-subscription/<int:pk>/', PlanDetailView.as_view(), name='plan-detail'),
    path('subscriptions/', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('subscriptions/<int:pk>/', SubscriptionDetailView.as_view(), name='subscription-detail'),
    path('current-subscription/<int:pk>/', GetCurrentSubscription.as_view(), name='current-subscription-detail'),
]