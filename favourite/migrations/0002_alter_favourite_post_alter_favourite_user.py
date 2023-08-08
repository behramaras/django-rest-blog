# Generated by Django 4.2.3 on 2023-07-31 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0006_alter_post_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("favourite", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favourite",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="post.post"
            ),
        ),
        migrations.AlterField(
            model_name="favourite",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]