from django.db import models

from django.db import models
from django.core.exceptions import ValidationError
import re


class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True, verbose_name='Логин')
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=128, verbose_name='Пароль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def clean(self):
        # Server-side валидация
        if len(self.username) < 3:
            raise ValidationError({'username': 'Логин должен содержать минимум 3 символа'})

        if len(self.password) < 8:
            raise ValidationError({'password': 'Пароль должен содержать минимум 8 символов'})

        # Проверка сложности пароля
        if not re.search(r'[A-Z]', self.password) or not re.search(r'[a-z]', self.password) or not re.search(r'[0-9]',self.password):
            raise ValidationError({'password': 'Пароль должен содержать заглавные и строчные буквы, а также цифры'})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    def clean(self):
        if len(self.name.strip()) < 2:
            raise ValidationError({'name': 'Имя должно содержать минимум 2 символа'})

        if len(self.message.strip()) < 10:
            raise ValidationError({'message': 'Сообщение должно содержать минимум 10 символов'})

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
