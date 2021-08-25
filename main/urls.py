from django.urls import path
from main import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('home/',views.homepage,name='home'),
    path('teams/',views.teamspage,name='teams'),
    path('lioneers/',views.lioneerspage,name='新竹街口攻城獅'),
    path('dreamers/',views.dreamerspage,name='福爾摩沙台新夢想家'),
    path('pilots/',views.pilotspage,name='桃園領航猿'),
    path('braves/',views.bravespage,name='台北富邦勇士'),
]