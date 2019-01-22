from django.conf.urls import url
from rest_framework_mongoengine import routers
from .views import ToolViewSet

router = routers.DefaultRouter()
router.register(r'mongo', ToolViewSet)

urlpatterns = [

]

urlpatterns += router.urls