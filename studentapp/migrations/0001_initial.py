# Generated by Django 3.1.4 on 2021-10-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('subject1', models.IntegerField()),
                ('subject2', models.IntegerField()),
                ('subject3', models.IntegerField()),
                ('subject4', models.IntegerField()),
                ('subject5', models.IntegerField()),
                ('subject6', models.IntegerField()),
            ],
        ),
    ]
