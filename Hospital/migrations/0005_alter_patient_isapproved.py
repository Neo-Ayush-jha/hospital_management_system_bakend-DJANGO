# Generated by Django 4.1.5 on 2023-03-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0004_rename_p_image_doctor_d_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='isApproved',
            field=models.BooleanField(default=True),
        ),
    ]
