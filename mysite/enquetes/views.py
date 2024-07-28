from django.shortcuts import render


def index(request):
    return HttpResponse('Enquetes - DSWeb 2024.1')