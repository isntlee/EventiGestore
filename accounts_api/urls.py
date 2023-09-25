from django.urls import path
from .views import AccountList

app_name = 'accounts_api'

urlpatterns = [
    path('accounts/', AccountList.as_view({'get': 'list'})),
    path('accounts/register/', AccountList.as_view({'post': 'create'}), name='register'),
    path('accounts/login/', AccountList.as_view({'post': 'login'}), name='login'),
    path('accounts/<slug:pk>/', AccountList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]