from django.db import models

class WebringModel(models.Model):
    STATUS_CHICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHICES, default='offline')
    last_updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    ping = models.IntegerField(default=0)

    def __str__(self):
        return self.name
