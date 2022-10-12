from django.shortcuts import render

def handler400(request, exception=None):

    return render(request, '400_page.html', status=400)

def handler403(request, exception=None):
    return render(request, '403_page.html', status=403)

def handler404(request, exception=None):
    return render(request, '404_page.html', status=404)

def handler500(request, exception=None):
    return render(request, '500_page.html', status=500)
