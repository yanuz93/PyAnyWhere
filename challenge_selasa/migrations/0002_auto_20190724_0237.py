# Generated by Django 2.2.3 on 2019-07-23 19:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('challenge_selasa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='foto_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
