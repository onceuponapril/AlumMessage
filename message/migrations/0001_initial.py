# Generated by Django 2.2.3 on 2019-07-06 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=20)),
                ('receiver', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=500)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'message',
                'managed': True,
            },
        ),
    ]
