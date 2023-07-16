from django.urls import path
from .views import index, MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('api/menu/', MenuItemView.as_view(), name='menu'),
    path('api/menu/<int:pk>', SingleMenuItemView.as_view(), name='single_menu'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]