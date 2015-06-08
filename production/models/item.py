from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Item(models.Model):
    class Meta:
        app_label = 'bassculture'
    orientation_choices = (
        ('l', 'landscape'),
        ('p', 'portrait'),
    )

    item_id = models.IntegerField(unique=True, db_index=True)
    authors = models.ManyToManyField("bassculture.Author", blank=True, related_name="items")
    full_title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=255)
    edition = models.CharField(max_length=16)
    date = models.CharField(max_length=16)
    link = models.URLField(blank=True, null=True)
    link_label = models.TextField(blank=True, null=True)
    rism = models.CharField(max_length=16)
    gore = models.CharField(max_length=16)
    pagination = models.CharField(max_length=8)
    orientation = models.CharField(max_length=16, blank=True, null=True, choices=orientation_choices)
    dimensions = models.CharField(max_length=8)
    library = models.CharField(max_length=40, blank=True, null=True)
    shelfmark = models.CharField(max_length=16)
    item_notes = models.TextField(blank=True, null=True)
    additional_items = models.TextField(blank=True, null=True)
    source = models.ForeignKey("bassculture.Source")
    seller = models.ForeignKey("bassculture.Seller", related_name="items", blank=True, null=True)
    publisher = models.ForeignKey("bassculture.Publisher", related_name="items", blank=True, null=True)
    printer = models.ForeignKey("bassculture.Printer", related_name="items", blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.short_title)


@receiver(post_save, sender=Item)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    record = si.query(type="item", item_id="{0}".format(instance.item_id)).execute()  # checks if the record already exists in solr

    if record:  # if it does
        si.delete_by_ids([x['id'] for x in record])

    d = {
        'url': 'http://localhost:8000/item/{0}'.format(instance.pk),
        'type': 'item',
        'id': str(uuid.uuid4()),
        'item_id': instance.item_id,
        'title': instance.short_title,
        'item_notes': instance.item_notes,
        'link': instance.link,
        'link_label': instance.link_label,
    }

    si.add(d)
    si.commit()
