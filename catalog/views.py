from django.shortcuts import render


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    return render(request, 'catalog/contacts.html')


def password(request):
    if request.method == 'GET':
        password_pr = request.GET.get('password')
        print(f'Пароль: {password_pr}')
    return render(request, 'catalog/password.html')


def index(request):
    return render(request, 'catalog/index.html')
