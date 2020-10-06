from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from commons.utils import get_current_server_time_info, get_local_time_info
from mocks.serializers import CreateMockRequestSerializer, TimeInfo


class Index(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    lookup_field = '_id'
    lookup_value_regex = '[0-9]+'

    def list(self, request, *args, **kwargs):
        # Show current server time
        current_server_time_info = get_current_server_time_info()
        response_serializer = TimeInfo(data=current_server_time_info)

        if response_serializer.is_valid(raise_exception=True):
            return Response(response_serializer.validated_data)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        # Convert time with timezone
        request_serializer = CreateMockRequestSerializer(data=request.data)
        if request_serializer.is_valid(raise_exception=True):
            local_time_info = get_local_time_info(**request_serializer.validated_data)

            response_serializer = TimeInfo(data=local_time_info)
            if response_serializer.is_valid(raise_exception=True):
                return Response(response_serializer.validated_data)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, _id=None, *args, **kwargs):
        # Show url param
        return Response({'_id': _id})

    def destroy(self, request, _id=None, *args, **kwargs):
        return Response(status=status.HTTP_423_LOCKED)

    @action(methods=('GET', ), detail=False)
    def hello(self, request, *args, **kwargs):
        return Response({'hello': 'hello'})

    @action(methods=('DELETE', ), detail=True)
    def bye(self, request, _id=None, *args, **kwargs):
        # Show url param
        return Response({'_id': _id})
