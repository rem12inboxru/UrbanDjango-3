from django.shortcuts import render
from django.http import HttpResponse, request, HttpRequest

from .forms import UserRegister


# Create your views here.
def sign_up_by_html(request):
    users = ['Anton', 'Ivan', 'Max', 'Ed']
    info = {}
    context = {}
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get('age')
        context = {'username': username, 'password': password,
                   'repeat_password': repeat_password, 'age': age, 'info': info}

        if password == repeat_password and int(age) >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username} !!!')

        elif password != repeat_password:
            info['error'] = f"Пароли не совпадают"

        elif int(age) < 18:
            info['error'] = f'Вы должны быть старше 18 лет'

        elif username in users:
            info['error'] = f'Пользователь уже существует'

    return render(request, template_name='fifth_task/registration_page.html', context=context)


def sign_up_by_django(request):
    users = ['Anton', 'Ivan', 'Max', 'Ed']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            repeat_password = request.POST.get("repeat_password")
            age = request.POST.get('age')

            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username} !!!')

            elif password != repeat_password:
                info['error'] = f"Пароли не совпадают"

            elif int(age) < 18:
                info['error'] = f'Вы должны быть старше 18 лет'

            elif username in users:
                info['error'] = f'Пользователь уже существует'

    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})



