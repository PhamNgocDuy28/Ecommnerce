# Generated by Django 5.0.2 on 2024-03-19 02:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="phone_number",
            field=models.CharField(
                max_length=50,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9]+$", "Enter a valid phone number."
                    )
                ],
            ),
        ),
    ]
