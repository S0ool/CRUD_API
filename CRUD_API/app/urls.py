from django.urls import path

from app.views import CreateView, UpdateDelete

urlpatterns = [
    path('posts/', CreateView.as_view()),
    path('posts/<int:pk>', UpdateDelete.as_view()),

]
