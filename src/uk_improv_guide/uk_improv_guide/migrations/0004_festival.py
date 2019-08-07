# Generated by Django 2.2.4 on 2019-08-07 19:25

from django.db import migrations, models
import django.db.models.deletion
import uk_improv_guide.lib.adminable
import uk_improv_guide.lib.site_mappable
import uk_improv_guide.lib.slack_notification_mixin


class Migration(migrations.Migration):

    dependencies = [
        ('uk_improv_guide', '0003_auto_20190804_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.URLField(blank=True, max_length=256)),
                ('website_link', models.URLField(blank=True, max_length=256)),
                ('eventbrite_link', models.URLField(blank=True, max_length=256)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='event/')),
                ('festival_type', models.CharField(choices=[('F', 'Festival'), ('R', 'Retreat')], max_length=1)),
                ('start_time', models.DateTimeField(verbose_name='Festival start time')),
                ('end_time', models.DateTimeField(verbose_name='Festival end time')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uk_improv_guide.School')),
                ('teachers', models.ManyToManyField(blank=True, to='uk_improv_guide.Performer', verbose_name='teachers teaching')),
                ('teams', models.ManyToManyField(blank=True, to='uk_improv_guide.Team', verbose_name='teams playing')),
                ('venue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uk_improv_guide.Venue')),
            ],
            options={
                'ordering': ['-start_time'],
            },
            bases=(uk_improv_guide.lib.slack_notification_mixin.SlackNotificationMixin, uk_improv_guide.lib.site_mappable.SiteMapThing, uk_improv_guide.lib.adminable.AdminableObject, models.Model),
        ),
    ]
