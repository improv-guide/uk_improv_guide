# Generated by Django 2.2.4 on 2019-08-01 23:07

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uk_improv_guide.lib.adminable
import uk_improv_guide.lib.site_mappable
import uk_improv_guide.lib.slack_notification_mixin
import uk_improv_guide.models.fields.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventSeries',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='event_series/')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(uk_improv_guide.lib.slack_notification_mixin.SlackNotificationMixin, uk_improv_guide.lib.adminable.AdminableObject, models.Model),
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_handle', models.CharField(blank=True, default='', max_length=100, validators=[uk_improv_guide.models.fields.fields.validate_twitter_handle], verbose_name='Twitter username')),
                ('facebook_link', models.URLField(blank=True, max_length=256)),
                ('website_link', models.URLField(blank=True, max_length=256)),
                ('contact_email_address', models.EmailField(blank=True, max_length=100, verbose_name='Email Address')),
                ('instagram_link', models.URLField(blank=True, default='', max_length=100, verbose_name='Instagram Link')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('middle_names', models.CharField(blank=True, default='', max_length=60)),
                ('family_name', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='performer/')),
                ('alias', models.CharField(blank=True, default='', max_length=50, verbose_name='Alias / Performing as')),
                ('imdb_link', models.CharField(blank=True, default='', max_length=100, verbose_name='IMDB Link')),
            ],
            options={
                'ordering': ['family_name', 'first_name'],
            },
            bases=(uk_improv_guide.lib.slack_notification_mixin.SlackNotificationMixin, uk_improv_guide.lib.site_mappable.SiteMapThing, uk_improv_guide.lib.adminable.AdminableObject, models.Model),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('twitter_handle', models.CharField(blank=True, default='', max_length=100, validators=[uk_improv_guide.models.fields.fields.validate_twitter_handle], verbose_name='Twitter username')),
                ('facebook_link', models.URLField(blank=True, max_length=256)),
                ('website_link', models.URLField(blank=True, max_length=256)),
                ('contact_email_address', models.EmailField(blank=True, max_length=100, verbose_name='Email Address')),
                ('instagram_link', models.URLField(blank=True, default='', max_length=100, verbose_name='Instagram Link')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='school/')),
                ('country', django_countries.fields.CountryField(default='GB', max_length=2)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(uk_improv_guide.lib.slack_notification_mixin.SlackNotificationMixin, uk_improv_guide.lib.site_mappable.SiteMapThing, uk_improv_guide.lib.adminable.AdminableObject, models.Model),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_handle', models.CharField(blank=True, default='', max_length=100, validators=[uk_improv_guide.models.fields.fields.validate_twitter_handle], verbose_name='Twitter username')),
                ('name', models.CharField(max_length=100)),
                ('facebook_link', models.CharField(blank=True, max_length=256)),
                ('website_link', models.CharField(blank=True, max_length=256)),
                ('google_maps_link', models.CharField(blank=True, max_length=256)),
                ('address', models.CharField(max_length=256, verbose_name='Street Address')),
                ('city', models.CharField(default='London', max_length=256)),
                ('postcode', models.CharField(max_length=10, verbose_name='Postal Code')),
                ('email_address', models.CharField(blank=True, max_length=100, verbose_name='Email Address')),
                ('country', django_countries.fields.CountryField(default='GB', max_length=2)),
                ('image', models.ImageField(upload_to='venue/')),
                ('school', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='uk_improv_guide.School', verbose_name='School affiliation')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(uk_improv_guide.lib.slack_notification_mixin.SlackNotificationMixin, uk_improv_guide.lib.site_mappable.SiteMapThing, uk_improv_guide.lib.adminable.AdminableObject, models.Model),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_handle', models.CharField(blank=True, default='', max_length=100, validators=[uk_improv_guide.models.fields.fields.validate_twitter_handle], verbose_name='Twitter username')),
                ('facebook_link', models.URLField(blank=True, max_length=256)),
                ('website_link', models.URLField(blank=True, max_length=256)),
                ('contact_email_address', models.EmailField(blank=True, max_length=100, verbose_name='Email Address')),
                ('instagram_link', models.URLField(blank=True, default='', max_length=100, verbose_name='Instagram Link')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='team/')),
                ('players', models.ManyToManyField(blank=True, related_name='plays_for', to='uk_improv_guide.Performer', verbose_name='Team members')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(uk_improv_guide.lib.slack_notification_mixin.SlackNotificationMixin, uk_improv_guide.lib.site_mappable.SiteMapThing, uk_improv_guide.lib.adminable.AdminableObject, models.Model),
        ),
        migrations.AddField(
            model_name='performer',
            name='teaches_for',
            field=models.ManyToManyField(blank=True, related_name='teachers', to='uk_improv_guide.School', verbose_name='Teaches at this school'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.URLField(blank=True, max_length=256)),
                ('website_link', models.URLField(blank=True, max_length=256)),
                ('eventbrite_link', models.URLField(blank=True, max_length=256)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='event/')),
                ('event_type', models.CharField(choices=[('S', 'Show'), ('J', 'Jam'), ('W', 'Workshop'), ('A', 'Audition')], max_length=1)),
                ('start_time', models.DateTimeField(verbose_name='Show start time')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='uk_improv_guide.EventSeries')),
                ('teams', models.ManyToManyField(blank=True, to='uk_improv_guide.Team', verbose_name='teams playing')),
                ('venue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='uk_improv_guide.Venue')),
            ],
            options={
                'ordering': ['-start_time'],
            },
            bases=(uk_improv_guide.lib.slack_notification_mixin.SlackNotificationMixin, uk_improv_guide.lib.site_mappable.SiteMapThing, uk_improv_guide.lib.adminable.AdminableObject, models.Model),
        ),
    ]
