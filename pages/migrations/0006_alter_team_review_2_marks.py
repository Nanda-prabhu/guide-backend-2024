# Generated by Django 4.2 on 2023-05-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_team_review_2_marks_alter_team_review_3_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='review_2_marks',
            field=models.IntegerField(default=10),
        ),
    ]
