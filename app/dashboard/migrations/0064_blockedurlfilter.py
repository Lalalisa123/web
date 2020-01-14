# Generated by Django 2.2.4 on 2019-11-20 15:37

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0063_bounty_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedURLFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('expression', models.CharField(help_text='the expression to search for in order to block that github url (or website)', max_length=255)),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
