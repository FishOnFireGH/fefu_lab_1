from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View
from .forms import FeedbackForm, RegistrationForm
from .models import UserProfile, Feedback

# Данные для существующих страниц (из первой лабораторной)
STUDENTS_DATA = {
    1: {
        'info': 'Иван Петров',
        'faculty': 'Кибербезопасность',
        'status': 'Активный',
        'year': 3
    },
    2: {
        'info': 'Мария Сидорова',
        'faculty': 'Информатика',
        'status': 'Активный',
        'year': 2
    },
    3: {
        'info': 'Алексей Козлов',
        'faculty': 'Программная инженерия',
        'status': 'Выпускник',
        'year': 5
    }
}

COURSES_DATA = {
    'python-basics': {
        'name': 'Основы программирования на Python',
        'duration': 36,
        'description': 'Базовый курс по программированию на языке Python для начинающих.',
        'instructor': 'Доцент Петров И.С.',
        'level': 'Начальный'
    },
    'web-security': {
        'name': 'Веб-безопасность',
        'duration': 48,
        'description': 'Курс по защите веб-приложений от современных угроз.',
        'instructor': 'Профессор Сидоров А.В.',
        'level': 'Продвинутый'
    },
    'network-defense': {
        'name': 'Защита сетей',
        'duration': 42,
        'description': 'Изучение методов и технологий защиты компьютерных сетей.',
        'instructor': 'Доцент Козлова М.П.',
        'level': 'Средний'
    }
}


# Существующие представления из первой лабораторной (обновленные для шаблонов)
def home_page(request):
    return render(request, 'fefu_lab/home.html', {
        'title': 'Главная страница',
        'heading': 'Добро пожаловать в FEFU Lab!'
    })


def about_page(request):
    return render(request, 'fefu_lab/about.html', {
        'title': 'О нас',
        'heading': 'О нашей лаборатории'
    })


def student_profile(request, student_id):
    if student_id in STUDENTS_DATA:
        student_data = STUDENTS_DATA[student_id]
        return render(request, 'fefu_lab/student_profile.html', {
            'title': f'Студент {student_id}',
            'heading': f'Профиль студента',
            'student_id': student_id,
            'student_info': student_data['info'],
            'faculty': student_data['faculty'],
            'status': student_data['status'],
            'year': student_data['year']
        })
    else:
        raise Http404("Студент с таким ID не найден")


def course_detail(request, course_slug):
    if course_slug in COURSES_DATA:
        course_data = COURSES_DATA[course_slug]
        return render(request, 'fefu_lab/course_detail.html', {
            'title': course_data['name'],
            'heading': course_data['name'],
            'course_slug': course_slug,
            'course_name': course_data['name'],
            'duration': course_data['duration'],
            'description': course_data['description'],
            'instructor': course_data['instructor'],
            'level': course_data['level']
        })
    else:
        raise Http404("Курс не найден")


class ContactsView(View):
    def get(self, request):
        return render(request, 'fefu_lab/contacts.html', {
            'title': 'Контакты',
            'heading': 'Контакты'
        })


# Новые представления для форм
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Сохраняем в базу данных
            feedback = Feedback(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            feedback.save()

            return render(request, 'fefu_lab/success.html', {
                'title': 'Успешная отправка',
                'heading': 'Сообщение отправлено!',
                'message': 'Ваше сообщение успешно отправлено. Мы свяжемся с вами в ближайшее время.'
            })
    else:
        form = FeedbackForm()

    return render(request, 'fefu_lab/feedback.html', {
        'title': 'Обратная связь',
        'heading': 'Форма обратной связи',
        'form': form
    })


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Сохраняем пользователя в базу данных
            user = UserProfile(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']  # В реальном проекте хешируйте пароль!
            )
            user.save()

            return render(request, 'fefu_lab/success.html', {
                'title': 'Успешная регистрация',
                'heading': 'Регистрация завершена!',
                'message': f'Пользователь {user.username} успешно зарегистрирован. Добро пожаловать!'
            })
    else:
        form = RegistrationForm()

    return render(request, 'fefu_lab/register.html', {
        'title': 'Регистрация',
        'heading': 'Регистрация нового пользователя',
        'form': form
    })


# Обработчик 404
def custom_404_view(request, exception):
    return render(request, 'fefu_lab/404.html', {
        'title': 'Страница не найдена',
        'heading': '404 - Страница не найдена'
    }, status=404)