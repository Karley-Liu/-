# Generated by Django 3.0.4 on 2020-04-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_url', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(null=True)),
            ],
        ),
    ]
