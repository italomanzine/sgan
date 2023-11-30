# Generated by Django 3.1.4 on 2023-11-30 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20231130_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descricaotreino',
            name='data_treino',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='descricaotreino',
            name='modelusuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='descricaotreino',
            name='treino',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.treino'),
        ),
    ]
