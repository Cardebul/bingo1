from django.shortcuts import render


def page_not_found(request, exception):

    return render(request, 'pages/404.html', status=404)


def handler500(request, *args, **argv):

    return render(request, 'pages/500.html', status=500)
