from django.urls import path

from tarjimon import views


urlpatterns = [
    path('', views.search_view, name="home")
]
