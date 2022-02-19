from django.urls import path, include
from . import views


urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),

    path('', include('django.contrib.auth.urls'), name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('logout', views.logging_out, name = 'logout'),
    path('<slug:slug>',views.forum),
    path('theme/<slug:slug>',views.themes)
]
