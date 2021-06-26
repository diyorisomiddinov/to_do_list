from django.contrib import admin

from sendmail.models import EmailModel


@admin.register(EmailModel)
class EmailModelAdmin(admin.ModelAdmin):
    list_display = ['subject', 'to_email', 'message']
    search_fields = ['subject', 'to_email', 'message']
    list_filter = ['to_email']
