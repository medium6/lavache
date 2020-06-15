from .views import showArticles
from django.urls import path


urlpatterns = [
    path('', showArticles, name='articles'),
]