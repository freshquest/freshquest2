from rest_framework.routers import DefaultRouter, Route

class SingletonRouter(DefaultRouter):
    routes = [
         Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
                'post': 'create',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            name='{basename}-list',
            initkwargs={'suffix': 'Singleton'}
        ),
    ]
