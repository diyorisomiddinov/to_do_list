from django.db import models


class EmailModel(models.Model):
    to_email = models.CharField(max_length=50)
    subject = models.CharField(max_length=25)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'emails'
