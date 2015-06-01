from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Publisher(models.Model):
    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = 'Publishers'
        app_label = 'bassculture'  # app label

    publisher_id = models.IntegerField(unique=True, db_index=True)
    name = models.CharField("Publisher", max_length=255)


    def __str__(self):
        return "{0}".format(self.name)


@receiver(post_save, sender=Publisher)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    record = si.query(type="publisher", publisher_id="{0}".format(instance.publisher_id)).execute()  # checks if the record already exists in solr

    if record:  # if it does
        si.delete_by_ids([x['id'] for x in record])

    d = {
        'pk': '{0}'.format(instance.pk),
        'type': 'publisher',
        'id': str(uuid.uuid4()),
        'publisher_id': instance.publisher_id,
    }

    si.add(d)
    si.commit()
