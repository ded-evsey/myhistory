from django.db import models
import uuid
from pyzbar.pyzbar import decode
from api.core import r_net
# Create your models here.
class ThemeManager(models.Manager):
    def get_by_qr(self, qr_img):
        try:
            return self.objects.get(id=decode(qr_img)[0].data)
        except:
            return Theme.objects.none()


class Theme(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    short = models.TextField(
        'Короткая информация'
    )
    data = models.TextField(
        'Информация'
    )
    objects = ThemeManager()
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

class TGUser(models.Model):
    user_ident = models.CharField(
        'Пользователь',
        max_length=128
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    last_login = models.DateTimeField(
        auto_now=True
    )
    themes = models.ManyToManyField(
        Theme,
        null=True,
        blank=True
    )

class Message(models.Model):
    TYPE_MESSAGE = (
        ('0','Question'),
        ('1','Img')
    )
    user = models.ForeignKey(
        TGUser,
        on_delete=models.CASCADE
    )
    type = models.CharField(
        choices=TYPE_MESSAGE,
        max_length=2
    )
    data=models.TextField(
        null=True,
        blank=True
    )
    response_theme=models.ForeignKey(
        Theme,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    response = models.TextField(
        null=True,
        blank=True
    )
    def save(self, *args, **kwargs):
        self.response_theme = self.user.themes.last()
        if int(self.type):
            self.response = self.response_theme.short
        else:
            messages = Message.objects.filter(
                type=self.type,
                data__search=self.data
            )
            if messages.count():
                self.response = messages.last().response
            else:
                answer = r_net([self.user.themes.last()],[self.data])
                if answer:
                    self.response = answer
                else:
                    answer = r_net(
                        self.user.themes.all().values_list('data', flat=True),
                        [self.data]
                    )
                    if answer:
                        self.response=answer
        return super().save(*args, **kwargs)
    def get_response(self):
        return {
            'chat_id':self.user.user_ident,
            'response': self.response
        }