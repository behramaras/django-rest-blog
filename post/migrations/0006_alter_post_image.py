# Generated by Django 4.2.3 on 2023-07-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0005_post_modified_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="post/"),
        ),
    ]