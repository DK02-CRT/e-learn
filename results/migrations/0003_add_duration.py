# Generated migration to add duration fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultstopic',
            name='duration',
            field=models.DurationField(default='0:00:00'),
            preserve_default=False,
        ),
    ]
