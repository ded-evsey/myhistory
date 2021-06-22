import requests
from core import settings
from .basic import BasicConnector

class MainConnector(BasicConnector):
    url = settings.MAIN_CONTAINER_URL
    def __init__(self, chat_id):
        super().__init__(chat_id)
        self._body_request = None

    @property
    def body_request_text(self):
        return self._body_request

    @body_request_text.setter
    def body_request_text(self, value):
        self._body_request = {
            'chat_id':self.chat_id,
            'text_message':value
        }

    @property
    def body_request_file(self):
        return self._body_request

    @body_request_file.setter
    def body_request_file(self, value):
        self._body_request = {
            'chat_id':self.chat_id,
            'file': value
        }


    @property
    def body(self):
        if self.body_request_text:
            return {
                'data': self.body_request_text
            }
        if not self.body_request_file:
            return
        body = self.body_request_file
        return {
            'files': {'file':body.pop('file')},
            'data':body
        }

    @property
    def method(self):
        if self.body_request_text:
            return 'text-data/'
        if self.body_request_file:
            return 'file-data/'
        return

    def get_data(self, text_data=None, file_data=None):
        if text_data:
            self.body_request_text = text_data
        elif file_data:
            self.body_request_file = file_data

        if not self.method or not self.body:
            return
        resp = requests.post(
            settings.MAIN_CONTAINER_URL + '/' + self.method,
            **self.body,
            verify=False
        )
        return resp.json()