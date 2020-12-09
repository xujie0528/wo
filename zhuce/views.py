from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func(request):
    if request.method == 'GET':
      return render(request, 'zhuce.html')
    else:
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        print('username:{0},passwd:{1}'.format(username, passwd))
        return HttpResponse('进行注册')
