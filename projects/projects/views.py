from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(
    (
        'HEAD',
        'GET',
    )
)
def health(request):
    return Response({'PROJECT_PROFILE': settings.PROJECT_PROFILE, 'PROJECT_VERSION': settings.PROJECT_VERSION})
