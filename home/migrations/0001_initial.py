# Generated by Django 2.2 on 2020-06-02 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('MADHYA PRADESH', 'MADHYA PRADESH'), ('UTTAR PRADESH', 'UTTAR PRADESH'), ('BIHAR', 'BIHAR'), ('GUJARAT', 'GUJRAT'), ('JHARKHAND', 'JHARKHAND'), ('PUNJAB', 'PUNJAB'), ('HIMACHAL PRADESH', 'HIMACHAL PRADESH'), ('JAMMU KASHMIR', 'JAMMU KASHMIR')], max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('post', models.CharField(blank=True, max_length=200, null=True)),
                ('seats', models.CharField(blank=True, max_length=5, null=True)),
                ('exam_date', models.CharField(blank=True, max_length=15, null=True)),
                ('regis_start', models.CharField(blank=True, max_length=20, null=True)),
                ('regis_end', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('exam_fees_general', models.IntegerField(blank=True, max_length=5, null=True)),
                ('exam_fees_obc', models.IntegerField(blank=True, max_length=5, null=True)),
                ('exam_fees_sc', models.IntegerField(blank=True, max_length=5, null=True)),
                ('portal_fee', models.IntegerField(blank=True, max_length=5, null=True)),
                ('main_website', models.URLField(blank=True, null=True)),
                ('notification', models.URLField()),
                ('result', models.URLField(blank=True, null=True)),
                ('admit_card', models.URLField(blank=True, null=True)),
                ('job_type', models.CharField(max_length=30)),
                ('eligibility', models.TextField()),
                ('age_limit', models.TextField(blank=True, null=True)),
                ('guidelines', models.TextField(blank=True, null=True)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
