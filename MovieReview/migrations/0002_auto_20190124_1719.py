# Generated by Django 2.1.5 on 2019-01-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='movie_desc',
            field=models.TextField(default=' ', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='movie_release_date',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
