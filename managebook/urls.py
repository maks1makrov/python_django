from django.urls import path

from managebook import views

urlpatterns = [
    path('hello/', views.BookView.as_view(), name='hello'),
]