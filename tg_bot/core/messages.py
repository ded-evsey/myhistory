def get_response(lang, type_message, **kwargs):
    messages = {
        'ru': {
            '/start':f'Привет {kwargs.get("first_name","")} {kwargs.get("first_name","")},'
                     f' я твой бот-экскурсовод.'
                     f'Ты мне можешь задать любой вопрос, а я постараюсь на него ответить.'
                     f'Так же, ты можешь отправить мне QR-код, и я пойму. про что ты хочешь узнать',
            'wait':'Пожалуйста, подожди, мне нужно подумать',
            'not_found':'Прости, этого я не знаю',
            'not_qr':'Похоже, это не QR код, ну или я не могу его разглядеть',
            'not_my_qr':'А ты хитрый, но это не мой QR код',
            'cant':'Я так не умею'
        }
    }
    if not messages.get(lang):
        return "Простите, я не понимаю"
    return messages[lang].get(type_message,messages[lang]['cant'])
