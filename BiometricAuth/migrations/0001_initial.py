# Generated by Django 3.0.6 on 2020-05-31 17:02

import BiometricAuth.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FingerPrintImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserBiometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iris_photo_counter', models.PositiveSmallIntegerField(default=0)),
                ('face_photo_counter', models.PositiveSmallIntegerField(default=0)),
                ('fingerprint_photo_counter', models.PositiveSmallIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IrisImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iris_image', models.ImageField(upload_to=BiometricAuth.models.iris_directory_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iris_image', to='BiometricAuth.UserBiometry')),
            ],
        ),
    ]
