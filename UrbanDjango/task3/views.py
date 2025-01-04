from django.shortcuts import render
from django.views.generic import TemplateView

def open_platform(request):
    return render(request, 'third_task/platform.html')


def open_cart(request):
    return render(request, 'third_task/cart.html')


def open_games(request):
    game1 = 'Atomik Heart'
    game2 = 'Cyberpunk 2077'
    game3 = 'PayDay2'
    game4 = 'The Elder Scrolls 6'
    game5 = 'The Sims 4'
    context = {
        'game1': game1,
        'game2': game2,
        'game3': game3,
        'game4': game4,
        'game5': game5,
    }
    return render(request, 'third_task/games.html', context=context)

# Create your views here.
