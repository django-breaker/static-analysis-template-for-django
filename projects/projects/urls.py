from django.urls import path, include

from projects.views import health

urlpatterns = (
    path('health', health, name='health'),
    path('mocks', include('mocks.urls', namespace='mocks')),
)
