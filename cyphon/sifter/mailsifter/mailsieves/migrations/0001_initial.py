# -*- coding: utf-8 -*-
# Copyright 2017-2018 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
#
# Generated by Django 1.10.1 on 2017-03-20 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('procedures', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='It\'s a good idea to name rules after the data they examine and the comparison they make, e.g. "log_contains_WARNING."', max_length=40, unique=True)),
                ('value', models.CharField(blank=True, help_text='The value to compare the data against. If using regex, the output of the regex is used for comparison.', max_length=255, null=True)),
                ('is_regex', models.BooleanField(default=False, help_text='Whether the value should be interpreted as a regular expression.', verbose_name='regular expression')),
                ('case_sensitive', models.BooleanField(default=False, help_text='Whether the comparison should be case sensitive.')),
                ('negate', models.BooleanField(default=False, help_text='Whether the Rule should be evaluated as True if the data does NOT match the condition.')),
                ('operator', models.CharField(choices=[('CharField:x', 'contains'), ('CharField:^x', 'begins with'), ('CharField:x$', 'ends with'), ('CharField:^x$', 'equals')], help_text='The type of comparison to make.', max_length=40)),
                ('field_name', models.CharField(choices=[('Attachment', 'Attachment'), ('Attachments', 'Attachments'), ('Date', 'Date'), ('To', 'To'), ('From', 'From'), ('Subject', 'Subject'), ('Content', 'Content')], max_length=40)),
                ('protocol', models.ForeignKey(blank=True, default=None, help_text='An optional Protocol to apply to the data so the result can be examined by the Rule. If no Protocol is specified, the raw data is examined instead.', null=True, on_delete=django.db.models.deletion.CASCADE, to='procedures.Protocol')),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MailSieve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('logic', models.CharField(choices=[('AND', 'AND'), ('OR', 'OR')], default='AND', help_text='Choose "AND" if all nodes should return True. Choose "OR" if one or more nodes should return True.', max_length=3)),
                ('negate', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MailSieveNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='node type')),
                ('sieve', models.ForeignKey(help_text='A rule or rule set to assign to the node.', on_delete=django.db.models.deletion.CASCADE, related_name='nodes', related_query_name='node', to='mailsieves.MailSieve')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='mailsievenode',
            unique_together=set([('sieve', 'content_type', 'object_id')]),
        ),
    ]
