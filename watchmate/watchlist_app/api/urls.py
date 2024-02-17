from django.contrib import admin
from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views


router = DefaultRouter()
router.register('stream', views.StreamPlatformViewSet, basename='streamplatform')

urlpatterns = [
    # FBV
    # path('list/', views.movie_list, name='movie-list'),
    # path('list/<int:pk>/', views.movie_detail, name='movie-details'),
    
    # APIView
    path('list/', views.WatchListAPIView.as_view(), name='movie-list'),
    path('list/<int:pk>/', views.WatchListDetailAPIView.as_view(), name='movie-detail'),
    # path('stream/', views.StreamPlatformAPIView.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', views.StreamPlatformDetailAPIView.as_view(), name='streamplatform-detail'),
    
    # Generics
    # path('review/', views.ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    
    path('', include(router.urls)),
    
]