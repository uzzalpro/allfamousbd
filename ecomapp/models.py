from django.db import models

# Create your models here.
class Setting(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=150)
    description = models.TextField()
    address = models.CharField(max_length=300)
    hotline = models.IntegerField()
    email = models.EmailField(blank=True, null=True, max_length=70)
    smptserver = models.CharField(max_length=100)
    smtpemail = models.EmailField(blank=True, null=True, max_length=70)
    smptpassword = models.CharField(blank=True, max_length=50)
    smptport = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    address = models.TextField()
    contact = models.TextField()
    status = models.CharField(max_length=50, choices=status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title