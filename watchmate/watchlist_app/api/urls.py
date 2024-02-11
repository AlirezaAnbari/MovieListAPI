from django.contrib import admin
from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    # FBV
    # path('list/', views.movie_list, name='movie-list'),
    # path('list/<int:pk>/', views.movie_detail, name='movie-details'),
    
    # APIView
    path('list/', views.MovieListAPIView.as_view(), name='movie-list'),
    path('list/<int:pk>/', views.MovieDetailAPIView.as_view(), name='movie-details'),

]