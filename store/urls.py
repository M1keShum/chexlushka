from django.urls import path
from .views import index, by_rubric

urlpatterns = [
    path('', index, name='main'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
]
