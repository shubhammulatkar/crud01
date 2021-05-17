
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('send',views.send,name='send'),
    path('show',views.show,name='show'),
    path('delete',views.show,name='show')

]
