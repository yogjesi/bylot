from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Game
from .forms import GameForm
import random

arr = []
def random_table():
    global arr
    if arr:
        now = random.choice(arr)
        arr.remove(now)
    else:
        arr = [1, 2, 3, 1, 2, 3]
        now = random.choice(arr)
        arr.remove(now)
    return now

# Create your views here.
@require_safe
def index(request):
    form = GameForm()
    members = Game.objects.order_by('-pk')
    context = {
        'members':members,
        'form':form
    }
    return render(request, 'games/index.html', context)


@require_http_methods(['GET', 'POST'])
def roll(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            number = random_table()
            member = form.save(commit=False)  # commit=False는 임시저장용
            member.table = number
            member.save()
            return redirect('games:index')
    else:
        form = GameForm()
    context = {
        'form':form,
    }
    print(form)
    # print(request.GET.get('name'))
    return render(request, 'games/index.html', context)

@require_POST
def delete(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.delete()
    return redirect('games:index')