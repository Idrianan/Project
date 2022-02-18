from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")
def task(request,board_name):
    return HttpResponse()