# Generated by Django 3.1.4 on 2021-01-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=70)),
                ('subject', models.TextField(blank=True, max_length=100)),
                ('message', models.TextField(blank=True, max_length=500)),
                ('status', models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=50)),
                ('ip', models.CharField(blank=True, max_length=100)),
                ('note', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('hotline', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=70, null=True)),
                ('smptserver', models.CharField(max_length=100)),
                ('smtpemail', models.EmailField(blank=True, max_length=70, null=True)),
                ('smptpassword', models.CharField(blank=True, max_length=50)),
                ('smptport', models.CharField(blank=True, max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/')),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField()),
                ('contact', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
