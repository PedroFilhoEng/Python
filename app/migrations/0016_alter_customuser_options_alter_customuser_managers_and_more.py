# Generated by Django 4.1.7 on 2023-04-11 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0015_customuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Usuário Personalizado', 'verbose_name_plural': 'Usuários Personalizados'},
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='groups',
            new_name='custom_groups',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='user_permissions',
            new_name='custom_user_permissions',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups_user',
            field=models.ManyToManyField(blank=True, help_text='Os grupos aos quais este usuário pertence. Um usuário pode pertencer a zero ou mais grupos.', related_name='user_set_user', related_query_name='user_user', to='auth.group'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions_user',
            field=models.ManyToManyField(blank=True, help_text='Permissões específicas para este usuário.', related_name='user_set_user', related_query_name='user_user', to='auth.permission'),
        ),
    ]
