# Generated by Django 3.2.8 on 2021-10-22 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20211022_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='articles.category'),
        ),
    ]