from django.urls import path

from . import views

urlpatterns = [
    path('view', views.event_view, name='view'),
    path('comment', views.event_comment, name='comment'),
    path('participate', views.event_participate, name='participate'),
    path('like', views.event_like, name='like'),
]