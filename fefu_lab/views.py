from django.http import HttpResponse, Http404
from django.views import View

# Function-Based Views
def home_page(request):
    return HttpResponse("Добро пожаловать на главную страницу FEFU Lab!")

def about_page(request):
    return HttpResponse("Страница 'О нас' - информация о проекте.")

def student_profile(request, student_id):
    if student_id > 100:
        raise Http404("Студент не найден")
    return HttpResponse(f"Профиль студента с ID: {student_id}")

def course_detail(request, course_slug):
    return HttpResponse(f"Информация о курсе: {course_slug}")

# Class-Based View
class ContactsView(View):
    def get(self, request):
        return HttpResponse("Страница контактов")