# Generated by Django 3.0.8 on 2020-07-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200715_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archive',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Archive', 'verbose_name_plural': 'Archive'},
        ),
        migrations.AddField(
            model_name='archive',
            name='slug',
            field=models.SlugField(blank=True, help_text=' \n          When django prepopulate slugs, it normally omits prepositions, do not forget\n          to add it manually\n        ', null=True, unique=True),
        ),
    ]
