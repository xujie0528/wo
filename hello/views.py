from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 定义view视图处理函数
def func(requests):
    # requests 每一个视图都有一个参数用来接收请求对象
    # return 返回响应
    return HttpResponse('<h1>hello world</h1>')