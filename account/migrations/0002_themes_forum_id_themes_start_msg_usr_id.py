# Generated by Django 4.0.2 on 2022-02-19 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='themes',
            name='forum_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.forums'),
        ),
        migrations.AddField(
            model_name='themes',
            name='start_msg_usr_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
