# Generated by Django 2.2 on 2020-01-23 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daylife', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daylife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('date', models.CharField(max_length=32)),
                ('detail', models.CharField(max_length=32)),
                ('logo', models.ImageField(upload_to='daylife/images')),
            ],
        ),
        migrations.CreateModel(
            name='Daystory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.CharField(max_length=32)),
                ('pic', models.ImageField(upload_to='daylife/images')),
                ('daylife', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daylife.Daylife')),
            ],
        ),
    ]