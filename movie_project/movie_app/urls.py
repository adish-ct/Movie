from django.urls import path
from . import views
app_name = 'movie_app'

urlpatterns = [
    path('', views.film, name='movie'),
    path('movie/<int:movie_id>/', views.detail, name="details"),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]