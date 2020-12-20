# Generated by Django 3.1.4 on 2020-12-20 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareserverapi', '0007_remove_post_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(null=True, upload_to='post_images')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='rareserverapi.post')),
            ],
        ),
    ]