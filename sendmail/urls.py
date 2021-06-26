from django.urls import path

from sendmail.views import EmailCreateView

app_name = 'email'

urlpatterns = [
    path('', EmailCreateView.as_view(), name='create')
]