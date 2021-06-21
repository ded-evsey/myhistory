from rest_framework import routers
from api.api.views import ImgMessageSendAPI, TextMessageSendAPI
router = routers.SimpleRouter()
router.register(
    'text-data', TextMessageSendAPI, basename='text_data',
)
router.register(
    'img-data', ImgMessageSendAPI, basename='img_data'
)
urlpatterns = router.urls