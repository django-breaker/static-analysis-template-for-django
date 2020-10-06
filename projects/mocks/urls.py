from django.urls import path


from commons.url_routers import APIRouter

from mocks import views


app_name = 'mocks'

index_router = APIRouter(trailing_slash=False)
index_router.register('', views.Index, basename='index')


urlpatterns = index_router.urls