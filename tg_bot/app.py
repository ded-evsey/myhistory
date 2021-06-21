from flask import Flask, request
from core import settings
from connectors import MessengerConnector, MainConnector
from core.messages import get_response
from io import BytesIO
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def basic():
    if request.method == 'POST':

        if not request.json.get('message'):
            return {'ok': True }
        message = request.json['message']
        tg_api = MessengerConnector(chat_id=message['chat']['id'])
        if message.get('text') == '/start':
            tg_api.send_message(
                get_response(
                    message['from']['language_code'],
                    message['text']
                )
            )
            return {"ok": True}
        connector = MainConnector(chat_id=message['chat']['id'])
        if message.get('text'):
            resp = connector.get_data(
                message.get('text')
            )
            tg_api.send_message(
                resp if resp else get_response(
                    message['from']['language_code'],
                    'not_found'
                )
            )
        if message.get('photo'):
            file_id = message.get('photo')[-1].get('file_id')
            with BytesIO() as file:
                file_data = tg_api.get_file(file_id)
                print(file_data)
                resp = connector.get_data(file_data=file_data)
                tg_api.send_message(
                    get_response(
                        message['from']['language_code'],
                        'not_my_qr'
                    ) if not resp or not resp.get('response') else resp.get('response')
                )
    return {"ok": True}

if __name__ == '__main__':
    app.run(host=settings.HOST,debug=settings.DEBUG)
