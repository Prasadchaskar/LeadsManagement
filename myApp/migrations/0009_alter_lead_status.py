# Generated by Django 3.2 on 2021-08-06 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_alter_lead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.status'),
        ),
    ]
