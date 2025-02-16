from django.shortcuts import render
from api.models import WebringModel


def home(request):
    participants = WebringModel.objects.all().values('name', 'status', 'description', 'url')

    return render(request, 'pages/home.html', {'participants': participants})
