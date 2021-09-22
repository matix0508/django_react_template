from django.urls import path
from .views import FirstModelView

urlpatterns = [
    path('firstModel', FirstModelView.as_view())
    ]