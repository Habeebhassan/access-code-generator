# Generated by Django 3.2.25 on 2024-08-02 01:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('residents', '0003_auto_20240802_0011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resident',
            options={'permissions': (('can_view_dashboard', 'Can view dashboard'),)},
        ),
        migrations.AddField(
            model_name='resident',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='resident',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='resident_set', related_query_name='resident', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='resident_set', related_query_name='resident', to='auth.Permission'),
        ),
    ]
