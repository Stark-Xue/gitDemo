"""我是新开发的直播模块"""
from django.shortcuts import render, HttpResponse
def index(request):
	return render(request, 'index.html')
def africa(request):
	return HttpResponse("非洲专区888")
def live(request):
	print('开发到一半')
	return HttpResponse('...')
