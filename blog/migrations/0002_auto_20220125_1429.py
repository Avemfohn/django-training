# Generated by Django 3.2.11 on 2022-01-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('SSN', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]