from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Theme,TGUser,Message
# Create your views here.


class ImgMessageSendAPI(APIView):
    def post(self, request, format=None):
        user,_ = TGUser.objects.get_or_create(
            user_ident=request.POST.get('chat_id')
        )
        theme = Theme.objects.get_by_qr(request.FILES['file'][0])
        if not theme:
            Response(
                {
                    'chat_id':user.user_ident,
                    'response':None
                }
            )
        user.themes.add(theme)
        message = Message.objects.create(
            user=user,
            type=Message.TYPE_MESSAGE[1]
        )
        return Response(
            message.get_response()
        )


class TextMessageSendAPI(APIView):
    def post(self,request, format=None):
        user, _ = TGUser.objects.get_or_create(
            user_ident=request.POST.get('chat_id')
        )
        message = Message.objects.create(
            user=user,
            type=Message.TYPE_MESSAGE[0],
            data=request.POST.get('text_message')
        )
        return Response(
            message.get_response()
        )