# Generated by Django 3.2.5 on 2021-08-10 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='postModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CareerModle', to='testing_app.careermodle')),
            ],
        ),
    ]
