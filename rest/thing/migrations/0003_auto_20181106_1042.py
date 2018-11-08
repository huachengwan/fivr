# Generated by Django 2.1.3 on 2018-11-06 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0002_recommended'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='thing',
            name='image',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='thing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thing.Thing'),
        ),
    ]