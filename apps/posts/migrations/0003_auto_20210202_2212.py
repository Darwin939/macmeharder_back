# Generated by Django 3.1.5 on 2021-02-02 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_postimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'verbose_name': 'Post Category',
                'verbose_name_plural': 'Post_Category',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='post_list', to='posts.post_category'),
        ),
    ]
