# Generated by Django 5.1.3 on 2024-11-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_fichaclinica_diagnostico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='adjuntos/')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='fichaclinica',
            name='adjuntos',
        ),
        migrations.AddField(
            model_name='fichaclinica',
            name='adjuntos',
            field=models.ManyToManyField(blank=True, to='core.adjunto'),
        ),
    ]