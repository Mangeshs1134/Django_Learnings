# Generated by Django 5.1.4 on 2024-12-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_recipelikes_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='yummy',
            name='category',
            field=models.CharField(choices=[('sweet', 'sweet'), ('spicy', 'spicy'), ('indo-chinease', 'indo-chinease'), ('punjabi', 'punjabi'), ('UP-special', 'UP-special'), ('new', 'new')], max_length=13, null='new'),
            preserve_default='new',
        ),
    ]
