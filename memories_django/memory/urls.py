from django.urls import path, include

from memory import views

urlpatterns = [
    path('latest-memories/', views.LatestMemoriesList.as_view(), name='latest-memories'),
    path('create-memory/', views.CreateMemory.as_view(), name='create-memory'),
]