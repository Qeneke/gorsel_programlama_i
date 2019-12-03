from django.http import HttpResponse


def index(request):
    return HttpResponse("Merhaba view. Burası uygulamamızın index sayfası.")
