# Generated by Django 4.0.4 on 2022-06-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp_Two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=100)),
                ('temp_email', models.CharField(blank=True, max_length=100, null=True)),
                ('otp', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='team',
            name='teamID',
            field=models.CharField(default='CSE', max_length=100),
        ),
    ]