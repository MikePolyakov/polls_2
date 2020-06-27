from django.db import models
from django.utils.timezone import now


class Question(models.Model):
    """Вопрос"""
    title = models.CharField(max_length=200,
                             verbose_name="Вопрос")
    date_published = models.DateField(verbose_name="Дата публикации",
                                      default=now)
    is_active = models.BooleanField(verbose_name="Опубликован")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """Вариант ответа на вопрос"""
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name="Вариант Ответа")

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Вариант Ответа'
        verbose_name_plural = 'Варианты Ответов'


class UserRespond(models.Model):
    """Реальный ответ на вопрос"""
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

