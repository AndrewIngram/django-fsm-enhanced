# Generated by Django 3.2.6 on 2021-08-16 13:17

from django.db import migrations, models
import django_fsm_enhanced.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('state', django_fsm_enhanced.fields.EnhancedFSMField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('ARCHIVED', 'Archived')], default='ACTIVE', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('content', models.TextField(blank=True, default='')),
                ('state', django_fsm_enhanced.fields.EnhancedFSMField(choices=[('DRAFT', 'Draft'), ('PUBLIC', 'Public'), ('PRIVATE', 'Private'), ('ARCHIVED', 'Archived')], default='DRAFT', max_length=50)),
            ],
        ),
    ]