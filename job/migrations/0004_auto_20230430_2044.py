# Generated by Django 3.2 on 2023-04-30 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='image',
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(null=True, upload_to='')),
                ('applydate', models.DateField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.studentuser')),
            ],
        ),
    ]
