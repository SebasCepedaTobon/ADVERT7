# Generated by Django 3.2.7 on 2021-09-06 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_contacto_tipo_consulta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contacto',
        ),
        migrations.AddField(
            model_name='producto',
            name='username',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]