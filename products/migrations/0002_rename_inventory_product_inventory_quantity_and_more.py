# Generated by Django 4.0.6 on 2022-07-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='inventory',
            new_name='inventory_quantity',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=None, max_length=400),
            preserve_default=False,
        ),
    ]