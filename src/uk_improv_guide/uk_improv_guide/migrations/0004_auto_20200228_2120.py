# Generated by Django 3.0.3 on 2020-02-28 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("uk_improv_guide", "0003_auto_20200228_1209"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={"ordering": ["country", "name"], "verbose_name_plural": "Cities"},
        ),
    ]
