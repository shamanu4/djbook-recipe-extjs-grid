from django.db import models

class City(models.Model):
    
    name = models.CharField(max_length=40, unique=True)
    
    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def store_record(self):
        obj = {}
        obj['id'] = self.pk
        obj['name'] = self.name
        return obj



class Street(models.Model):

    city = models.ForeignKey(City, default=1, related_name='streets')
    name = models.CharField(max_length=40)
    
    class Meta:
        ordering = ['name']
        unique_together = (("city", "name",),)

    def __unicode__(self):
        return "%s" % (self.name)

    def store_record(self):
        obj = {}
        obj['id'] = self.pk
        obj['city'] = self.city.pk
        obj['name'] = self.name
        return obj
