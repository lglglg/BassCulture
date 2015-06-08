from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Source(models.Model):
    class Meta:
        app_label = "bassculture"
        verbose_name = "Source"
        verbose_name_plural = "Sources"

    source_id = models.IntegerField(unique=True, db_index=True)
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
    source_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.title)


@receiver(post_save, sender=Source)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    record = si.query(type="source", source_id="{0}".format(instance.source_id)).execute() # checks if the record already exists in solr

    if record: # if it does
        si.delete_by_ids([x['id'] for x in record])

    d = {
        'url': 'http://localhost:8000/source/{0}'.format(instance.pk),
        'pk': '{0}'.format(instance.pk),
        'type': 'source',
        'id': str(uuid.uuid4()),
        'source_id': instance.source_id,
        'description': instance.description,
        'title' : instance.title,
    }

    si.add(d)
    si.commit()
