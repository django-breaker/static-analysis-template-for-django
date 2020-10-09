from django.urls import include, path

from projects.views import health


urlpatterns = (
    path('health', health, name='health'),
    path('mocks', include('mocks.urls', namespace='mocks')),
)
