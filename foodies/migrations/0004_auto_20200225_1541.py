# Generated by Django 2.1.5 on 2020-02-25 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodies', '0003_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Allergies',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('price', models.FloatField(default=0)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='page',
            name='category',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='typeofmeat',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='vegetable',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.AddField(
            model_name='meal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodies.Category'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='meal',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='foodies.Meal'),
            preserve_default=False,
        ),
    ]
