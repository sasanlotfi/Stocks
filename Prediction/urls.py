from django.urls import path,include
from .views import ticker_show,home_show
urlpatterns=[
    path('',home_show),
    path('stock_info',ticker_show)
]