from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import Treatment


class IndexView(TemplateView):
    template_name = "app/index.html"
    # form_class = FormContact
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["treatments"] = Treatment.objects.all().exclude(description="")
        return context

    #
    # def form_valid(self, form):
    #     if self.request.POST.get("form_type") == "form_1":
    #         self.object = form.save(commit=False)
    #         self.object.save()
    #
    #     elif self.request.POST.get("form_type") == "form_2":
    #         self.object = form.save(commit=False)
    #         self.object.save()
    #
    #     return super().form_valid(form)
