# Generated by Django 2.2.4 on 2019-08-09 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("uk_improv_guide", "0004_festival")]

    operations = [
        migrations.AddField(
            model_name="event",
            name="duration",
            field=models.FloatField(
                default=2.0,
                help_text="What is the expected run time of this show?",
                verbose_name="Show duration in hours",
            ),
        )
    ]
