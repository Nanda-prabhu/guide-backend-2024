# Generated by Django 4.0.4 on 2022-10-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0038_alter_team_project_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]