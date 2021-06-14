import requests
from core import settings

def get_data(method, sending_data):
    resp = requests.get(
        settings.MAIN_CONTAINER_URL + '/' + method,
        data=sending_data
    )
    return resp
def get_data_for_text(text):
    try:
        return get_data(
            'text_data',
            {
                'text_message':text
            }
        ).json().get('response')
    except:
        return None