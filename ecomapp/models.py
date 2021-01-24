from django.db import models
from django.forms import ModelForm, TextInput, EmailInput
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
        


class ContactMessage(models.Model):
    status = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70)
    subject = models.TextField(max_length=100, blank=True)
    message = models.TextField(max_length=500, blank=True)
    status = models.CharField(max_length=50, choices=status, default='New')
    ip = models.CharField(max_length=100, blank=True )
    note = models.CharField(max_length=200, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name & Sure name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Write your email'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Write your Subjects'}),
            'message': TextInput(attrs={'class': 'input', 'placeholder': 'Write your messages'}),
        }         