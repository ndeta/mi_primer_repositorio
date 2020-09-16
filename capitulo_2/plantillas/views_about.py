from django.http import HttpResponse


def ndeya_about(request):
   return render(request, 'about.html')