# Generated by Django 4.1.5 on 2023-03-06 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0006_room_isavailable'),
    ]

    operations = [
        migrations.CreateModel(
            name='CABIL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CABIL_NUMBER', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=12)),
                ('isAvailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='cableNumber',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.cabil'),
        ),
    ]
