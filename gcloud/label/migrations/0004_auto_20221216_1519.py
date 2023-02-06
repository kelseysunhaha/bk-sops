# Generated by Django 3.2.15 on 2022-12-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("label", "0003_auto_20221215_2035"),
    ]

    operations = [
        migrations.AlterField(
            model_name="label",
            name="from_space_id",
            field=models.IntegerField(blank=True, help_text="创建标签的空间 ID", null=True, verbose_name="来源空间 ID"),
        ),
        migrations.AlterField(
            model_name="label",
            name="project_id",
            field=models.IntegerField(blank=True, help_text="标签对应project id", null=True, verbose_name="项目 ID"),
        ),
        migrations.AlterUniqueTogether(name="label", unique_together={("project_id", "name", "from_space_id")},),
    ]