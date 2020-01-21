# Generated by Django 2.2.9 on 2020-01-13 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=64)),
                ('descript', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('loge', models.ImageField(upload_to='animal/images')),
                ('store', models.TextField()),
                ('origin', models.CharField(max_length=32)),
                ('data', models.CharField(max_length=32)),
                ('author', models.CharField(max_length=32)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apicture', models.ImageField(upload_to='animal/images')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal')),
                ('animalstore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.AnimalStore')),
            ],
        ),
    ]
