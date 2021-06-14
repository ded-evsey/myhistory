from flask import Flask, request
from core import settings
from core.tg_api import Messenger
from core.messages import get_response
from core.connector_to_main import get_data_for_text
from io import BytesIO
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def basic():
    if request.method == 'POST':
        tg_api = Messenger()
        if not request.json.get('message'):
            return {'ok': True }
        message = request.json['message']
        chat_id = message['chat']['id']
        if message.get('text') == '/start':
            tg_api.send_message(
                chat_id,
                get_response(
                    message['from']['language_code'],
                    message['text']
                )
            )
            return {"ok": True}
        if message.get('text'):
            resp = get_data_for_text(
                message.get('text')
            )
            tg_api.send_message(
                chat_id,
                resp if resp else get_response(
                    message['from']['language_code'],
                    'not_found'
                )
            )
        if message.get('photo'):
            tg_api.send_message(
                chat_id,
                get_response(
                    message['from']['language_code'],
                    'not_my_qr'
                )
            )
            file_id = message.get('photo')[-1].get('file_id')
            with BytesIO() as file:
                file_data = tg_api.get_file(file_id)

    return {"ok": True}

if __name__ == '__main__':
    app.run(host=settings.HOST,debug=settings.DEBUG)
