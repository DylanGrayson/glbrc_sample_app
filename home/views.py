from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Icon, Application


@login_required()
def index(request):
    icons = request.user.icon_set.filter(default_status=True)
    apps = request.user.icon_set.filter(default_status=False)
    return render(request, 'home.html', {'icons': icons, 'apps': apps})

@login_required()
def add_app(request):
    if request.method == "POST":
        app = Application.objects.get(id=request.POST['app-id'])
        icon = request.user.icon_set.get(app=app)
        icon.default_status = True
        icon.save()
        return HttpResponseRedirect('/')

@login_required()
def remove_app(request):
    if request.method == "POST":
        app = Application.objects.get(id=request.POST['app-id'])
        icon = request.user.icon_set.get(app=app)
        icon.default_status = False
        icon.save()
        return HttpResponseRedirect('/')
