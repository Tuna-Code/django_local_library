# Generated by Django 4.2.18 on 2025-01-22 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.language'),
        ),
    ]
