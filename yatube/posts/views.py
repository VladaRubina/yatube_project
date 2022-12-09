from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse('Категории')


def posts_detail(request, slug):
    return HttpResponse(f'Пост {slug}')