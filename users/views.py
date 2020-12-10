from django.shortcuts import render
from django.http import HttpResponse
from users.models import User
from django.shortcuts import redirect
from django.http import JsonResponse

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
        user = User.objects.create(username=username, password=password)
        # 进行业务处理
        return redirect('/login/')



def login(request):
    """登录View视图函数"""
    if request.method == 'GET':
        # 返回登录页面
        return render(request, 'login.html')
    else:
        # 登录业务逻辑
        # 获取 username 和 password
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 进行用户名和密码校验
        try:
            # 根据 username 和 password 查询对应的用户是否存在，即进行用户名和密码校验
            # get 方法默认会利用查询到的数据创建一个对应的模型类对象，并将这个模型对象返回
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            # 如果 get 方法查询不到数据，会出现 `模型类.DoesNotExist` 异常
            # 用户名或密码错误
            return JsonResponse({'message': 'login failed'})
        else:
            # 用户名和密码正确
            return JsonResponse({'message': 'login success'})

