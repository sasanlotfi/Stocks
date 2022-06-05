from django.urls import path,include
from .views import ticker_show,home_show,image_html,new_Ticker,show_Ticker,ticker_Detail,ticker_Update
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('',home_show,name = "home"),
    path('stock_info',ticker_show),
    path('ticker',new_Ticker.as_view()),
    path('show_ticker/<int:pk>',show_Ticker.as_view(),name = "Detail"),
    path('list_show',show_Ticker.as_view(),name = "Show_List"),
    path('detail/<int:pk>',ticker_Detail.as_view(),name= "ticker_detail"),
    path('update/<int:pk>',ticker_Update.as_view(), name = "ticker_update")
]


