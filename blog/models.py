from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200) #Используется для определения строк фиксированной длины от короткой до средней. Вы должны указать max_length для хранения данных.

    text = models.TextField() #используется для больших строк произвольной длины. Вы можете указать max_length для поля, но это используется только тогда, когда поле отображается в формах (оно не применяется на уровне базы данных).

    created_date = models.DateTimeField(default=timezone.now) #используются для хранения / представления дат и информации о дате / времени
    #Значение по умолчанию для поля. Это может быть значение или вызываемый объект, и в этом случае объект будет вызываться каждый раз, когда создается новая запись.

    published_date = models.DateTimeField(blank=True, null=True)
    #Если True, поле может быть пустым в ваших формах. По умолчанию используется значение False, что означает, что проверка формы Django заставит вас ввести значение. Это часто используется с null = True, потому что если вы хотите разрешить пустые значения, вы также хотите, чтобы база данных могла представлять их соответствующим образом.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

