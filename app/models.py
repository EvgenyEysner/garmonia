from django.db import models


class Treatment(models.Model):
    class CategoryChoices(models.IntegerChoices):
        KOSMETIK = 1, "Kosmetische Behandlungen"
        NAGELDESIGN = 2, "Nageldesign"
        PERMANENT = 3, "Permanent Make Up"
        ENTHAARUNG = 4, "Körperenthaarung"
        FUSSPFLEGE = 5, "Fußpflege"

    name = models.CharField("Name", max_length=255)
    category = models.PositiveSmallIntegerField(
        choices=CategoryChoices.choices,
        default=CategoryChoices.KOSMETIK,
        verbose_name="Leistungen",
    )

    description = models.TextField("Beschreibung", null=True, blank=True)

    price = models.DecimalField("Preise", max_digits=10, decimal_places=2, null=True)

    class Meta:
        ordering = ["category"]
        verbose_name = "Behandlung"
        verbose_name_plural = "Behandlungen"

    def __str__(self):
        return self.name


class MonthlyOffer(models.Model):
    treatment = models.ForeignKey(
        Treatment,
        on_delete=models.CASCADE,
        verbose_name="Monatliches Angebot",
    )
    title = models.CharField("Angebotsbezeichnung", max_length=128)
    description = models.TextField("Angebotsbeschreibung")
    image = models.ImageField(verbose_name="Angebotsbild", upload_to="media")
    active = models.BooleanField("Angebot aktiv?", default="False")
    price = models.DecimalField("Preise", max_digits=10, decimal_places=2, null=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Angebot"
        verbose_name_plural = "Angebote"

    def __str__(self):
        return self.title


class Gallery(models.Model):
    pass
