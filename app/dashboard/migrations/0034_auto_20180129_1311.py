# Generated by Django 2.0 on 2018-01-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0033_auto_20180125_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='interested',
            field=models.ManyToManyField(blank=True, to='dashboard.Interest'),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='interested_comment',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='issue_description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
