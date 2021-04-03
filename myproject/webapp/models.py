from django.db import models



# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Poll(BaseModel):
    quetion = models.TextField(max_length=400, verbose_name='Опрос', blank=False, null=False)


    class Meta:
        db_table = 'poll'
        verbose_name = 'Опрос'
        verbose_name_plural = 'опросы'

    def __str__(self):
        return self.quetion


class Choice(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='poll', on_delete=models.CASCADE, verbose_name='Опрос')
    text = models.TextField(max_length=500, verbose_name='ответ', null=False, blank=False)


    class Meta:
        db_table = 'answer'
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'

    def __str__(self):
        return self.text[:20]

