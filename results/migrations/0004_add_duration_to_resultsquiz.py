# Generated migration to add duration to ResultsQuiz

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_add_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultsquiz',
            name='duration',
            field=models.DurationField(default='0:00:00'),
            preserve_default=False,
        ),
    ]
