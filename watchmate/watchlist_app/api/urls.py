from django.contrib import admin
from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    # FBV
    # path('list/', views.movie_list, name='movie-list'),
    # path('list/<int:pk>/', views.movie_detail, name='movie-details'),
    
    # APIView
    path('list/', views.WatchListAPIView.as_view(), name='watchlist-list'),
    path('list/<int:pk>/', views.WatchListDetailAPIView.as_view(), name='watchlist-detail'),
    path('stream/', views.StreamPlatformAPIView.as_view(), name='stream-list'),
    path('stream/<int:pk>/', views.StreamPlatformDetailAPIView.as_view(), name='streamplatform-detail'),
    
]