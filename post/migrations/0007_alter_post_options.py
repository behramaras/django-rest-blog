# Generated by Django 4.2.3 on 2023-08-03 12:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0006_alter_post_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["id"]},
        ),
    ]