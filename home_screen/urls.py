from django.urls import path
from . import views
from .views import CustomerListView,CustomerDetailView

urlpatterns = [
    path('', views.home,name='home-screen'),
    path('viewList/', CustomerListView.as_view(),name='view-list'),
    path('user/<int:pk>/',CustomerDetailView.as_view(),name='user-detail'),
    path('transfer/<int:pk>',views.transfer,name='transfer'),
]

