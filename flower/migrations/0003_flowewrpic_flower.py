# Generated by Django 2.2.9 on 2020-01-09 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0002_flowewrpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowewrpic',
            name='flower',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='flower.Flower'),
            preserve_default=False,
        ),
    ]
