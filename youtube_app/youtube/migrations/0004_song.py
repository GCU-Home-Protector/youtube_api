# Generated by Django 5.1.3 on 2024-12-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("youtube", "0003_alter_youtubevideo_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Song",
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
                ("title", models.CharField(max_length=200)),
                ("youtube_id", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, null=True)),
                ("like_count", models.IntegerField(default=0)),
                ("channel", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "emotion",
                    models.CharField(
                        choices=[
                            ("positive", "Positive"),
                            ("negative", "Negative"),
                            ("neutral", "Neutral"),
                            ("unknown", "Unknown"),
                        ],
                        default="unknown",
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]