from django.urls import path

from Events import views 

urlpatterns = [
	path('',views.eventManager,name='Events'),
	


]