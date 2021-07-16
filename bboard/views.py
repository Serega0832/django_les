from django.shortcuts import render
from .models import Bb, Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy
import time

def index(request):
    print(request)
    print(request.GET)
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def check_ad():
    print(111111)
    return 33333333333

def check_user():
    print(222222)

def qqq(request, **kwargs):

    print(request)
    print(request.GET['id']) # "333" это id объявления, отправляемого в таком формате http://127.0.0.1:2000/qqq/?id=333
    # print(kwargs)
    from bboard.models import Qqq
    q = Qqq()
    w = check_ad
    print(w)
    q.title = 'Name'
    q.save()
    w = Qqq.objects.get(id=q.id)
    w.title = '123'
    from torpy.http.requests import TorRequests
    with TorRequests() as tor_requests:
        print("build circuit")
        with tor_requests.get_session() as sess:
            q = sess.get("https://api.youla.io/api/v1/product/60914eba1441ee46c3326f07").json()
            print(q)
            return render(request, 'bboard/qqq.html', q)
            # print(sess.get("http://httpbin.org/ip").json())
        print("renew circuit")
        with tor_requests.get_session() as sess:
            print(sess.get("http://httpbin.org/ip").json())
            print(sess.get("http://httpbin.org/ip").json())
    for i in range(100):
        if w.title!='Name':
            context = {'qqq': w}
            return render(request, 'bboard/qqq.html', context)
        print('жду 1 сек')
        w = Qqq.objects.get(id=q.id)
        time.sleep(1) # Сон в 1 секунду

    # bbs = Bb.objects.all()
    # rubrics = Rubric.objects.all()
    # context = {'bbs': bbs, 'rubrics': rubrics}
    # return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context