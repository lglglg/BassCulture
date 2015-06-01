# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('author_id', models.IntegerField(unique=True, db_index=True)),
                ('surname', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'authors',
                'ordering': ['surname'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('item_id', models.IntegerField(unique=True, db_index=True)),
                ('full_title', models.CharField(max_length=255)),
                ('short_title', models.CharField(max_length=255)),
                ('edition', models.CharField(max_length=16)),
                ('date', models.CharField(max_length=16)),
                ('link', models.URLField(blank=True, null=True)),
                ('link_label', models.TextField(blank=True, null=True)),
                ('rism', models.CharField(max_length=16)),
                ('gore', models.CharField(max_length=16)),
                ('pagination', models.CharField(max_length=8)),
                ('orientation', models.CharField(blank=True, choices=[('l', 'landscape'), ('p', 'portrait')], null=True, max_length=16)),
                ('dimensions', models.CharField(max_length=8)),
                ('library', models.CharField(blank=True, null=True, max_length=40)),
                ('shelfmark', models.CharField(max_length=16)),
                ('item_notes', models.TextField(blank=True, null=True)),
                ('additional_items', models.TextField(blank=True, null=True)),
                ('authors', models.ManyToManyField(blank=True, related_name='items', to='bassculture.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('printer_id', models.IntegerField(unique=True, db_index=True)),
                ('name', models.CharField(verbose_name='Printer', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'printers',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('publisher_id', models.IntegerField(unique=True, db_index=True)),
                ('name', models.CharField(verbose_name='Publisher', max_length=255)),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('seller_id', models.IntegerField(unique=True, db_index=True)),
                ('name', models.CharField(verbose_name='Seller', db_index=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Seller',
                'verbose_name_plural': 'Sellers',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('source_id', models.IntegerField(unique=True, db_index=True)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('source_notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='printer',
            field=models.ForeignKey(blank=True, related_name='items', to='bassculture.Printer', null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='publisher',
            field=models.ForeignKey(blank=True, related_name='items', to='bassculture.Publisher', null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(blank=True, related_name='items', to='bassculture.Seller', null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='source',
            field=models.ForeignKey(to='bassculture.Source'),
        ),
    ]
