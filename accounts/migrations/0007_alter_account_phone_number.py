# Generated by Django 5.0.2 on 2024-03-19 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_alter_account_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="phone_number",
            field=models.CharField(max_length=50),
        ),
    ]
