# Generated by Django 5.0.7 on 2024-07-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "iranian_cities",
            "0007_alter_city_table_comment_alter_county_table_comment_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={
                "ordering": ["id"],
                "verbose_name": "City",
                "verbose_name_plural": "Cities",
            },
        ),
        migrations.AlterModelOptions(
            name="county",
            options={
                "ordering": ["id"],
                "verbose_name": "County",
                "verbose_name_plural": "Counties",
            },
        ),
        migrations.AlterModelOptions(
            name="district",
            options={
                "ordering": ["id"],
                "verbose_name": "District",
                "verbose_name_plural": "Districts",
            },
        ),
        migrations.AlterModelOptions(
            name="province",
            options={
                "ordering": ["id"],
                "verbose_name": "Province",
                "verbose_name_plural": "Provinces",
            },
        ),
        migrations.AlterModelOptions(
            name="ruraldistrict",
            options={
                "ordering": ["id"],
                "verbose_name": "Rural District",
                "verbose_name_plural": "Rural Districts",
            },
        ),
        migrations.AlterModelOptions(
            name="village",
            options={
                "ordering": ["id"],
                "verbose_name": "Village",
                "verbose_name_plural": "Villages",
            },
        ),
        migrations.AlterField(
            model_name="city",
            name="code",
            field=models.BigIntegerField(
                db_comment="This field stores the code for the location.",
                help_text="The code representing the location.",
                unique=True,
                verbose_name="Code",
            ),
        ),
        migrations.AlterField(
            model_name="county",
            name="code",
            field=models.BigIntegerField(
                db_comment="This field stores the code for the location.",
                help_text="The code representing the location.",
                unique=True,
                verbose_name="Code",
            ),
        ),
        migrations.AlterField(
            model_name="district",
            name="code",
            field=models.BigIntegerField(
                db_comment="This field stores the code for the location.",
                help_text="The code representing the location.",
                unique=True,
                verbose_name="Code",
            ),
        ),
        migrations.AlterField(
            model_name="province",
            name="code",
            field=models.BigIntegerField(
                db_comment="This field stores the code for the location.",
                help_text="The code representing the location.",
                unique=True,
                verbose_name="Code",
            ),
        ),
        migrations.AlterField(
            model_name="ruraldistrict",
            name="code",
            field=models.BigIntegerField(
                db_comment="This field stores the code for the location.",
                help_text="The code representing the location.",
                unique=True,
                verbose_name="Code",
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="code",
            field=models.BigIntegerField(
                db_comment="This field stores the code for the location.",
                help_text="The code representing the location.",
                unique=True,
                verbose_name="Code",
            ),
        ),
        migrations.AddIndex(
            model_name="city",
            index=models.Index(fields=["code"], name="iranian_cit_code_1c3b38_idx"),
        ),
        migrations.AddIndex(
            model_name="county",
            index=models.Index(fields=["code"], name="iranian_cit_code_7732af_idx"),
        ),
        migrations.AddIndex(
            model_name="district",
            index=models.Index(fields=["code"], name="iranian_cit_code_5e016c_idx"),
        ),
        migrations.AddIndex(
            model_name="province",
            index=models.Index(fields=["code"], name="iranian_cit_code_3fe5d7_idx"),
        ),
        migrations.AddIndex(
            model_name="ruraldistrict",
            index=models.Index(fields=["code"], name="iranian_cit_code_39b229_idx"),
        ),
        migrations.AddIndex(
            model_name="village",
            index=models.Index(fields=["code"], name="iranian_cit_code_358568_idx"),
        ),
    ]
