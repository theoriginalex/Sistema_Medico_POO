from django.shortcuts import render

from django.http import HttpResponse, JsonResponse


def hola(request):
  return render(request, template_name='mipaypal/index.html')