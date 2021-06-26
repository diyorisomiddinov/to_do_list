from django.urls import path

from tasks.views import TaskCreateView, check

urlpatterns = [
    path('', TaskCreateView.as_view(), name='create'),
    path('<int:pk>/', check, name='active')
]