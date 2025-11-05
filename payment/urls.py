
from django.urls import path
from . import views

urlpatterns = [
    path('bkash/',views.BkashPaymentView.as_view()),
    path('bkash/callback/',views.BkashCallbackView.as_view()),
    path('success/',views.success,name='payment_success'),
    path('cancel/',views.cancel,name='payment_failed'),
]