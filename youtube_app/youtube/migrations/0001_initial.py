# Generated by Django 5.1.3 on 2024-12-03 03:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="YouTubeVideo",
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
                ("title", models.CharField(max_length=255)),
                ("channel_name", models.CharField(max_length=255)),
                ("views", models.BigIntegerField()),
                ("likes", models.BigIntegerField()),
                ("views_per_like", models.FloatField()),
                ("video_link", models.URLField()),
            ],
        ),
    ]