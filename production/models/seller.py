from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Seller(models.Model):
    class Meta:
        verbose_name_plural = "Sellers"
        verbose_name = "Seller"
        app_label = "bassculture"

    seller_id = models.IntegerField(unique= True, db_index=True)
    name = models.CharField("Seller", max_length=255, db_index=True)


    def __str__(self):
        return "{0}".format(self.name)


@receiver(post_save, sender=Seller)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    record = si.query(type="seller", seller_id="{0}".format(instance.seller_id)).execute()  # checks if the record already exists in solr

    if record:  # if it does
        si.delete_by_ids([x['id'] for x in record])

    d = {
        'pk': '{0}'.format(instance.pk),
        'type': 'seller',
        'id': str(uuid.uuid4()),
        'seller_id': instance.seller_id,
    }

    si.add(d)
    si.commit()
