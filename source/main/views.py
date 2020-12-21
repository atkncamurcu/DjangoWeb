from django.views.generic import TemplateView
from django.shortcuts import redirect,render


class IndexPageView(TemplateView):
    template_name = 'main/index.html'
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("/accounts/log-in")
        else:
             return render(request, IndexPageView.template_name, {})


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
