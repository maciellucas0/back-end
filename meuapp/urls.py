from django.urls import path
from .views import upload

app_name = "home"
urlpatterns = [path("", upload, name="upload")]
