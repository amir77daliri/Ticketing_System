from django.db import models
from django.contrib.auth import get_user_model


class ContactUs(models.Model):
    STATUS_CHOICES = (
        ('p', 'در حال بررسی'),
        ('d', 'بررسی شده')
    )
    user = models.ForeignKey(get_user_model(), related_name='contacts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, default='p')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'پیشنهادات'
