# Generated by Django 2.1.7 on 2019-02-27 23:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=150)),
                ('votos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=300)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='alternativa',
            name='pergunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pesquisa.Pergunta'),
        ),
    ]
