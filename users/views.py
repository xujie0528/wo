from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'GET':
        # 使用模板文件, 返回响应
        return render(request, 'index.html')
    else:
        # 获取表单提交的用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username:{0}, passworld:{1}'.format(username, password))
        # 进行业务处理
        return HttpResponse('注册成功!')
