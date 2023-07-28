# Generated by Django 4.2.2 on 2023-06-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0010_alter_uploadfile_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadfile",
            name="file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="board/%Y/%m/%d",
                verbose_name="uploaded file",
            ),
        ),
    ]
