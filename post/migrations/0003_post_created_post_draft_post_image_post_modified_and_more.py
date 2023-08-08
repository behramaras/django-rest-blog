# Generated by Django 4.2.3 on 2023-07-21 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0002_alter_post_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 21, 11, 8, 24, 845583, tzinfo=datetime.timezone.utc
                ),
                editable=False,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="draft",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                default=datetime.datetime(
                    2023, 7, 21, 11, 8, 27, 635982, tzinfo=datetime.timezone.utc
                ),
                upload_to="media/post/",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="modified",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 21, 11, 8, 29, 690507, tzinfo=datetime.timezone.utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default=datetime.datetime(
                    2023, 7, 21, 11, 8, 31, 719259, tzinfo=datetime.timezone.utc
                ),
                editable=False,
                max_length=150,
                unique=True,
            ),
            preserve_default=False,
        ),
    ]