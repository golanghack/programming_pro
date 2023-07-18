# Generated by Django 4.2.3 on 2023-07-18 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bb", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rubric",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=30, verbose_name="Rubric"
                    ),
                ),
            ],
            options={
                "verbose_name": "Rubric",
                "verbose_name_plural": "Rubrics",
                "ordering": ["name"],
            },
        ),
        migrations.AlterModelOptions(
            name="bb",
            options={
                "ordering": ["-published"],
                "verbose_name": "Board",
                "verbose_name_plural": "Boards",
            },
        ),
        migrations.AlterField(
            model_name="bb",
            name="content",
            field=models.TextField(blank=True, null=True, verbose_name="content"),
        ),
        migrations.AlterField(
            model_name="bb",
            name="price",
            field=models.FloatField(blank=True, null=True, verbose_name="price"),
        ),
        migrations.AlterField(
            model_name="bb",
            name="published",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, verbose_name="Published"
            ),
        ),
        migrations.AlterField(
            model_name="bb",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Cost"),
        ),
        migrations.AddField(
            model_name="bb",
            name="rubric",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="bb.rubric",
                verbose_name="Rubric",
            ),
        ),
    ]
