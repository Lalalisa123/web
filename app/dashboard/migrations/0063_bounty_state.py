# Generated by Django 2.2.4 on 2019-11-11 13:06

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0062_hackathonevent_show_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='bounty_state',
            field=models.CharField(choices=[('open', 'Open Bounty'), ('work_started', 'Work Started'), ('work_submitted', 'Work Submitted'), ('done', 'Done'), ('cancelled', 'Cancelled'), ('expired', 'Expired')], db_index=True, default='open', max_length=50),
        ),
        migrations.CreateModel(
            name='BountyEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('event_type', models.CharField(choices=[('accept_worker', 'Accept Worker'), ('cancel_bounty', 'Cancel Bounty'), ('submit_work', 'Submit Work'), ('stop_work', 'Stop Work'), ('express_interest', 'Express Interest'), ('payout_bounty', 'Payout Bounty'), ('expire_bounty', 'Expire Bounty'), ('extend_expiration', 'Extend Expiration'), ('close_bounty', 'Close Bounty')], max_length=50)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('bounty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='dashboard.Bounty')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
