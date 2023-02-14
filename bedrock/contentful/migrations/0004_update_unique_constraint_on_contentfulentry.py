# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 2.2.24 on 2021-12-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contentful", "0003_add_classification_category_and_tags_fields_to_contentfulentry"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contentfulentry",
            name="contentful_id",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name="contentfulentry",
            unique_together={("contentful_id", "locale")},
        ),
    ]
