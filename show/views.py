from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .sentiment import sentimentAnalysis

def index(request):
    return render(request, 'show/test.html')

def web(request):
    if request.method=="GET":
        return render(request, 'show/web.html')
    else:
        text=(request.POST.get('inpText'))
        tokenW = request.POST.get('wordt')
        tokenS = request.POST.get('sentt')
        # option=request.POST.get('option')
        # print(tokenS,tokenW)
        response = sentimentAnalysis(text, tokenW, tokenS)
        context = {'resp':response}
        return render(request, 'show/webres.html', context=context)

def apiHelp(request):
    return render(request, 'show/manapi.html')

@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = 'http://localhost:8000/'  # this can be current domain
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')


def reports(request):
    return HTTPResponse('<h1>Report</h1>')
