from django.views.generic import TemplateView
from django.shortcuts import render



class HomePageView(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Page404(TemplateView):
    template_name = "404_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def reg_page(request):
    return render(request, 'reg_page.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

