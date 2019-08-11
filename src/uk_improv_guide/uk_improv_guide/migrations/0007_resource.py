# Generated by Django 2.2.4 on 2019-08-11 18:49

from django.db import migrations, models
import uk_improv_guide.lib.adminable
import uk_improv_guide.lib.site_mappable
import uk_improv_guide.lib.slack_notification_mixin


class Migration(migrations.Migration):

    dependencies = [
        ('uk_improv_guide', '0006_auto_20190809_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_link', models.URLField(blank=True, max_length=256)),
                ('rss_feed_link', models.URLField(blank=True, max_length=256)),
                ('name', models.CharField(max_length=100)),
                ('resource_type', models.CharField(choices=[('B', 'Blog'), ('P', 'Podcasts'), ('R', 'Reference')], max_length=1)),
                ('image', models.ImageField(blank=True, upload_to='team/')),
                ('contributors', models.ManyToManyField(blank=True, related_name='hosts_podcasts', to='uk_improv_guide.Performer', verbose_name='Team members')),
            ],
            options={
                'verbose_name': 'Blog/Podcast',
                'ordering': ['name'],
            },
            bases=(uk_improv_guide.lib.slack_notification_mixin.SlackNotificationMixin, uk_improv_guide.lib.site_mappable.SiteMapThing, uk_improv_guide.lib.adminable.AdminableObject, models.Model),
        ),
    ]
