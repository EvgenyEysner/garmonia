import random

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import EmailPostForm, AppointmentForm
from .models import Treatment, MonthlyOffer, Testimonial, GalleryImage


class IndexView(TemplateView):
    template_name = "app/index.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["offers"] = MonthlyOffer.objects.filter(active=True)
        context["items"] = Treatment.objects.all()

        # get random Treatments as best-selling
        treatments = list(Treatment.objects.all())
        # get random Testimonials
        testimonials = list(Testimonial.objects.all())
        # get random image for Gallery
        images = list(GalleryImage.objects.all())
        context["selling"] = random.sample(treatments, 6)
        context["testimonials"] = random.sample(testimonials, 3)
        context["photos"] = random.sample(images, 10)
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST" and request.POST.get("form_type") == "form-1":
            form = AppointmentForm(request.POST)

            if form.is_valid():
                # Form fields passed validation
                cd = form.cleaned_data
                name = f"{cd['name']}"
                email = f"{cd['email']}"
                phone = f"{cd['phone']}"
                subject = f"{form.data.get('package')}"
                message = (
                    f"Eine neue Nachricht von {name}\nEmail: {email} "
                    f"\nTelefon: {phone}"
                    f"\nGewünschte Behandlung:{subject}"
                )
                send_mail(
                    subject,
                    message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.RECIPIENT_ADDRESS],
                )
                return HttpResponseRedirect(self.success_url)
        else:
            form = AppointmentForm()

        if request.method == "POST" and request.POST.get("form_type") == "form-2":
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
                return HttpResponseRedirect(self.success_url)
            else:
                form = EmailPostForm()
        return render(request, self.template_name, {"form": form})
