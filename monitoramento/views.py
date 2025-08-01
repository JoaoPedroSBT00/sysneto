from django.shortcuts import render


def monitoramento(request):
    return render(request, 'monitoramento.html')