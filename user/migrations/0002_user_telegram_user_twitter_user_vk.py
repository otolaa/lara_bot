# Generated by Django 4.2.1 on 2024-10-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="telegram",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Телеграм"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="twitter",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Твиттер"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="vk",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="ВКонтакте"
            ),
        ),
    ]
