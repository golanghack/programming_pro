# Generated by Django 4.2 on 2023-04-22 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0004_alter_list_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="list",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="lists.list",
            ),
        ),
    ]
