# Generated by Django 4.1.1 on 2022-09-28 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AppCoder", "0003_resena_delete_estudiante"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="resena",
            name="comentarios",
        ),
    ]
