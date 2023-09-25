from django.urls import path
from .views import AccountList

app_name = 'accounts_api'

urlpatterns = [
    path('accounts/register/', AccountList.as_view({'post': 'create'}), name='register'),
    path('accounts/login/', AccountList.as_view({'post': 'login'}), name='login'),
]

