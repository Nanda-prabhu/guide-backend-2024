# Generated by Django 4.0.4 on 2023-02-18 08:00

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0046_alter_team_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='myImage',
            field=models.ImageField(upload_to=pages.models.guide_directory_path),
        ),
    ]