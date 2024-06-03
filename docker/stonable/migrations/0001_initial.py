# Generated by Django 5.0.6 on 2024-06-03 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annuaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('adresse', models.CharField(blank=True, max_length=200)),
                ('code_postal', models.CharField(blank=True, max_length=8)),
                ('ville', models.CharField(blank=True, max_length=50)),
                ('telephone_fixe', models.CharField(blank=True, max_length=20)),
                ('telephone_portable', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('date_naissance', models.DateField(blank=True)),
                ('note', models.TextField(blank=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]