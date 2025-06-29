from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('me/', views.MeView.as_view(), name='me'),
    path('users/', views.UsersInOrgView.as_view(), name='users_in_org'),
    path('kudos/give/', views.GiveKudosView.as_view(), name='give_kudos'),
    path('kudos/received/', views.KudosReceivedView.as_view(), name='kudos_received'),
    path('kudos/given/', views.KudosGivenView.as_view(), name='kudos_given'),
    path('kudos/remaining/', views.KudosRemainingView.as_view(), name='kudos_remaining'),
]