# Generated by Django 4.1.7 on 2023-02-17 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='skill',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
