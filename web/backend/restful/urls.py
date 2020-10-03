from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.urls import path
from back import models
from back.serializers import UsersSerializer, InputFileSerializer, CarsSerializer
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Serializers define the API representation.
# JSON형태로 변환해주는 라이브러리 Serializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # User모델안에 객체로 모두 가져와서 queryset 에 저장
    # queryset 은 모델형태
    serializer_class = UserSerializer
    # serializer_class 는 UserSerializer(JSON) 형태를 쓰겠다.


class UsersViewSet(viewsets.ModelViewSet):
    queryset = models.users.objects.all()
    serializer_class = UsersSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.InputFile.objects.all()
    serializer_class = InputFileSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = models.cars.objects.all()
    serializer_class = CarsSerializer


schema_view = get_schema_view(
    openapi.Info(
        # 필수 인자
        title="Autosearch API",
        default_version="v1",
        # 선택 인자
        description="API 서비스입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="team10@ssafy.com"),
        license=openapi.License(name="SSAFY License"),
    )
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
#router.register(r'back/upload', ImageViewSet)
#router.register(r'back/users', UsersViewSet)
#router.register(r'back/cars', CarViewSet)
# users 로 호출하면 UserViewSet 이 호출됨 13Line<<<<<<<<<<<<<<<

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('back/', include("back.urls")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
