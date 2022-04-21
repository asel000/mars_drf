from django.urls import path
from .views import PostAPIView, PostCreateAPIView,PostDetailAPIView


urlpatterns = [
    path('', PostAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:id>/', PostDetailAPIView.as_view(), name='create')
]
