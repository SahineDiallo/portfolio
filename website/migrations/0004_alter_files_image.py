# Generated by Django 4.0.4 on 2022-04-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_project_back_end_alter_project_front_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='image',
            field=models.FileField(upload_to='project_images'),
        ),
    ]
