from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Author(models.Model):
    class Meta:
        verbose_name_plural = 'authors'
        app_label = 'bassculture'  # app label
        ordering = ['surname']

    author_id = models.IntegerField(unique=True, db_index=True)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s, %s" % (self.surname, self.name)
#       return "{0}, {1}".format(self.surname, self.name)

    @property
    def full_name(self):
        if self.name:
            return u"{0}, {1}".format(self.surname, self.name)
        else:
            return u"{0}".format(self.surname)


@receiver(post_save, sender=Author)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import scorched

    si = scorched.SolrInterface(settings.SOLR_SERVER)
    record = si.query(type="author", author_id="{0}".format(instance.author_id)).execute()  # checks if the record already exists in solr

    if record:  # if it does
        si.delete_by_ids([x['id'] for x in record])

    d = {
        'pk': '{0}'.format(instance.pk),
        'type': 'author',
        'id': str(uuid.uuid4()),
        'author_id': instance.author_id,
        'name': instance.name,
        'surname': instance.surname
    }

    si.add(d)
    si.commit()
