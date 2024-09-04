from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appname': 'GoToko',
        'name': 'Yeshua Marco Gracia Manurung',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)