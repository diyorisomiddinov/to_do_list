from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from sendmail.forms import EmailModelForm


class EmailCreateView(CreateView):
    template_name = 'emails.html'
    form_class = EmailModelForm
    success_url = '/email/'

    def form_valid(self, form):
        obj = form.save()
        text = f'Subject: {obj.subject}\n\nMessage: {obj.message}'
        send_mail(
            'Message',
            text,
            settings.EMAIL_HOST_USER,
            [obj.to_email],
        )
        return redirect(self.success_url)






