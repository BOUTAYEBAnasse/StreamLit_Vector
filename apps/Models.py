class Services(models.Model):
    name = models.CharField(max_length=254)
    location = models.PointField(srid=4326)

    def __unicode__(self):
            return self.name

    class Meta:
        verbose_name_plural = " Services"