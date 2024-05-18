from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name='myindex'),
    # path('', views.my_form_view, name='myinmy_form_viewdex'),

   

]