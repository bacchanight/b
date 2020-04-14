from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('level',views.show, name = 'show'),
    path('' , views.index , name = 'index'),
    path('start' , views.form_user_start , name = 'form_user_start'),
    path('continue' , views.form_user_continue , name = 'form_user_continue'),
    path('add_user', views.add_user, name = "add_user"),
    path('recover_user', views.recover_user, name = "recover_user"),
    path('next_level', views.next_level, name = "next_level"),
    path('check_detail', views.check_detail, name = "check_detail"),
    path('new_click', views.new_click, name = "new_click"),
    path('buy_clue', views.buy_clue, name = "buy_clue")
]
