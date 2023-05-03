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
        return self.category.__str__()
