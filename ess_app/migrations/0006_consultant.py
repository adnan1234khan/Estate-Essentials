# Generated by Django 4.1.7 on 2023-03-15 05:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ess_app', '0005_tips'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('user_id', models.CharField(default=None, max_length=45, primary_key=True, serialize=False)),
                ('password', models.CharField(default=None, max_length=45)),
                ('name', models.CharField(default=None, max_length=100)),
                ('email', models.CharField(default=None, max_length=100)),
                ('phone', models.CharField(default=None, max_length=100)),
                ('address', models.TextField()),
                ('experience', models.CharField(default=None, max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
