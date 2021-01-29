from django.urls import path
from . import views
urlpatterns = [
    path('', views.Movie_home, name="MovieUpHome"),
    path('createItem', views.createItem, name="createItem"),
    path('MovieIndex', views.MovieUp_index, name="MovieIndex"),
    path('<int:pk>/MovieDetails', views.MovieUp_details, name='MovieDetails'),
    path('<int:pk>/EditMovie', views.MovieUp_edit, name='EditMovie'),
    path('<int:pk>/DeleteMovie', views.MovieUp_delete, name='DeleteMovie'),
    path('<int:pk>/ConfirmDelete', views.confirm_delete, name='ConfirmDelete'),
    path('Movie_api/', views.MovieUp_api, name='Movie_api'),



]

