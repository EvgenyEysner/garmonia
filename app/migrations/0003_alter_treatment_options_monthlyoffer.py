# Generated by Django 4.2 on 2023-05-04 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_treatment_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="treatment",
            options={
                "ordering": ["category"],
                "verbose_name": "Behandlung",
                "verbose_name_plural": "Behandlungen",
            },
        ),
        migrations.CreateModel(
            name="MonthlyOffer",
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
                    "title",
                    models.CharField(
                        max_length=128, verbose_name="Angebotsbezeichnung"
                    ),
                ),
                ("description", models.TextField(verbose_name="Angebotsbeschreibung")),
                (
                    "image",
                    models.ImageField(upload_to="media", verbose_name="Angebotsbild"),
                ),
                (
                    "active",
                    models.BooleanField(default="False", verbose_name="Angebot aktiv?"),
                ),
                (
                    "treatment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.treatment",
                        verbose_name="Monatliches Angebot",
                    ),
                ),
            ],
            options={
                "verbose_name": "Angebot",
                "verbose_name_plural": "Angebote",
                "ordering": ["title"],
            },
        ),
    ]