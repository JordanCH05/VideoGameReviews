# Generated by Django 3.2 on 2022-01-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsite', '0012_alter_review_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.DecimalField(choices=[(0, '0.0 - Worst Game Ever'), (0.5, '0.5 - Horrible'), (1, '1.0 - Terrible'), (1.5, '1.5 - Rubbish'), (2, '2.0 - Bad'), (2.5, '2.5 - Mediocre'), (3, '3.0 - Playable'), (3.5, '3.5 - Ok'), (4, '4.0 - Good'), (4.5, '4.5 - Great'), (5, '5.0 - Master Piece')], decimal_places=1, max_digits=2),
        ),
    ]
