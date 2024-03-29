# Generated by Django 2.1.5 on 2019-01-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pro_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=11)),
                ('price', models.FloatField()),
                ('describe', models.CharField(max_length=11)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'product',
                'ordering': ('created',),
            },
        ),
    ]
