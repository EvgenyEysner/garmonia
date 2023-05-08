import random

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import EmailPostForm
from .models import Treatment, MonthlyOffer, Testimonial


class IndexView(TemplateView):
    template_name = "app/index.html"
    # form_class = FormContact
    success_url = reverse_lazy("home")
    context_object = "item_category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["offers"] = MonthlyOffer.objects.filter(active=True)
        context["items"] = Treatment.objects.all()

        # get random Treatments as best-selling
        treatments = list(Treatment.objects.all())
        # get random Testimonials
        testimonials = list(Testimonial.objects.all())
        context["selling"] = random.sample(treatments, 6)
        context["testimonials"] = random.sample(testimonials, 3)
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            # Form was submitted
            form = EmailPostForm(request.POST)
            if form.is_valid():
                # Form fields passed validation
                cd = form.cleaned_data
                first_name = f"{cd['first_name']}"
                last_name = f"{cd['last_name']}"
                email = f"{cd['email']}"
                subject = f"{cd['subject']}"
                message = (
                    f"Eine neue Nachricht von {first_name}, {last_name} \nEmail: {email} "
                    f"\nNachricht: {cd['message']}"
                )
                send_mail(
                    subject,
                    message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.RECIPIENT_ADDRESS],
                )
                return HttpResponseRedirect("/")
        else:
            form = EmailPostForm()
        return render(request, self.template_name, {"form": form})

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
