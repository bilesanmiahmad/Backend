# Generated by Django 4.2.1 on 2023-08-27 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('business_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=50)),
                ('billing_address', models.CharField(max_length=128)),
                ('shipping_address', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('document_type', models.CharField(choices=[('TIN', 'Tax Identification Number'), ('PITIN', 'Personal Income Tax Identification Number'), ('CAC_CERTIFICATE', 'CAC Certificate'), ('OTHER', 'Other Document')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
