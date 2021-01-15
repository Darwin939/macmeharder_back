# Generated by Django 3.1.5 on 2021-01-15 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'verbose_name': 'App Category',
                'verbose_name_plural': 'App_Category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=200)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('language_count', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('size', models.FloatField(blank=True, null=True)),
                ('award', models.CharField(blank=True, max_length=100, null=True)),
                ('place', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('developer', models.CharField(blank=True, max_length=300, null=True)),
                ('chart', models.CharField(blank=True, max_length=300, null=True)),
                ('version', models.CharField(blank=True, max_length=300, null=True)),
                ('compatibility', models.CharField(blank=True, max_length=400, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='apps_list', to='apps.app_category')),
            ],
            options={
                'verbose_name': 'apps',
                'verbose_name_plural': 'apps',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='AppImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='apps/')),
                ('is_avatar', models.BooleanField(default=False)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_images', to='apps.apps')),
            ],
            options={
                'verbose_name': 'App Images',
                'verbose_name_plural': 'App_Images',
            },
        ),
    ]