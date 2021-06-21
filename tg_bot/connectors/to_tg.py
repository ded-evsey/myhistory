import requests
from core import settings
from .basic import BasicConnector

class MessengerConnector(BasicConnector):
    url = 'https://api.telegram.org'

    def get_url(self,method, path=None):
        return '{url}{file}/bot{token}/{method}'.format(
            url=self.url,
            file='/file' if method =='file' else '',
            token=settings.TG_API_TOKEN,
            method=method if method != 'file' else path
        )

    def send_message(self, msg):
        method = 'sendMessage'
        url = self.get_url(method)
        data = {
            "chat_id":self.chat_id,
            "text":msg
        }
        requests.post(url,data)

    def _get_file_url(self, file_id):
        method = 'getFile'
        resp = requests.post(
            self.get_url(method),
            params={
                'file_id':file_id
            }
        )
        try:
            return resp.json()['result']['file_path']
        except KeyError:
            return None

    def get_file(self, file_id):
        file_path = self._get_file_url(file_id)
        if not file_path:
            return None

        resp = requests.get(
            self.get_url('file',file_path)
        )
        return resp.content
