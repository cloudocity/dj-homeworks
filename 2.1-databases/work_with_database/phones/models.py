from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=254, null=False)
    price = models.CharField(max_length=254, null=True)
    image = models.CharField(max_length=254, null=True)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Phone, self).save(*args, **kwargs)

