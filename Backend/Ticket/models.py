from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from extensions.utils import jalali_converter
import random


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('P', 'در حال بررسی'),  # pending
        ('A', 'پاسخ داده شده'),  # Answered
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    tracking_code = models.IntegerField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)
    # related fields :
    user = models.ForeignKey(get_user_model(), related_name='tickets', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at', 'id']

    def __str__(self):
        return f"{self.title}/{self.tracking_code}"

    def jpublish(self):
        return jalali_converter(self.created_at)

    def save(self, *args, **kwargs):
        while True:
            if not self.tracking_code:
                try:
                    tracking_code = random.randint(1000, 99999)
                    self.tracking_code = tracking_code
                    self.slug = slugify(f'ticket {self.tracking_code}')
                    super(Ticket, self).save(*args, **kwargs)
                    break
                except:
                    pass
            else:
                self.slug = slugify(f'ticket {self.tracking_code}')
                super(Ticket, self).save(*args, **kwargs)
                break


class TicketResponse(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Related Fields :
    user = models.ForeignKey(get_user_model(), null=True, related_name='ticket_responses', on_delete=models.SET_NULL)
    ticket = models.ForeignKey(Ticket, related_name='responses', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at', 'id']
        verbose_name = 'پاسخ'
        verbose_name_plural = 'پاسخ ها'

    def jcreated(self):
        return jalali_converter(self.created_at)

    def __str__(self):
        return f"response to: {self.ticket.tracking_code}"
