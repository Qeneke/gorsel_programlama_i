from django.http import HttpResponse
from django.conf import settings


def index(request):
    content = '<html>test123İş</html>'

    content = content.translate(''.maketrans(
        getattr(settings, 'KAYNAK'), getattr(settings, 'HEDEF')))

    response = HttpResponse(content, content_type='text/html; charset=ascii')
    response['Content-Length'] = len(content)

    return response
