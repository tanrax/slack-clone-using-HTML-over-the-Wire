# Generated by Django 4.0 on 2022-04-03 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('chat', '0007_alter_message_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='target',
        ),
        migrations.RemoveField(
            model_name='room',
            name='client',
        ),
        migrations.AddField(
            model_name='room',
            name='clients_active',
            field=models.ManyToManyField(related_name='clients_active', to='chat.Client'),
        ),
        migrations.AddField(
            model_name='room',
            name='clients_subscribed',
            field=models.ManyToManyField(related_name='clients_subscribed', to='chat.Client'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
