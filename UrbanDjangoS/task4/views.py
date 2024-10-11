from django.shortcuts import render


# Create your views here.
def render_start(request):
    return render(request, 'fourth_task/start.html')


'''def render_games(request):
    return render(request, 'fourth_task/games.html')'''


def index_basket(request):
    title = 'КОРЗИНА'
    message1 = 'В вашей корзине пока ничего нет'
    message2 = 'Сумма ваших покупок :'
    message3 = 'Благодарим за покупку'
    summ = ' 0.00 '
    glav = 'На главную страницу'
    context = {'title': title, 'message1': message1, 'message2': message2,
               'message3': message3, 'summ': summ, 'glav': glav}
    return render(request, 'fourth_task/basket.html', context)


def index_games(request):
    title = 'МАГАЗИН'
    '''games1 = 'Need for Speed: Underground'
    games2 = 'Need for Speed: Most Wanted'
    games3 = 'Need for Speed: Carbon'''
    buy = 'КУПИТЬ'
    glav = 'На главную страницу'
    context = {'title': title, 'games': ['Need for Speed: Underground', 'Need for Speed: Most Wanted',
                                         'Need for Speed: Carbon'], 'buy': buy, 'glav': glav}
    return render(request, 'fourth_task/games.html', context)

# Create your views here.
