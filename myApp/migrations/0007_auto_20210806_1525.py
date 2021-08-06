# Generated by Django 3.2 on 2021-08-06 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_alter_lead_agent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='agent_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myApp.agent'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.status'),
        ),
    ]