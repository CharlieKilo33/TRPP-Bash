# Generated by Django 3.1.6 on 2021-03-18 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('body', tinymce.models.HTMLField()),
                ('url', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('created_date', models.DateTimeField(verbose_name='Дата')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Имя ползователя')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='HistoricalGroupArticles',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Group name')),
                ('description', models.TextField(verbose_name='Group description')),
                ('private', models.BooleanField(default=False, verbose_name='Private goup?')),
                ('slug', models.SlugField(max_length=60, verbose_name='Url to group')),
                ('created_date', models.DateTimeField(verbose_name='Group created date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Group author')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Group Article',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalArticle',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('body', tinymce.models.HTMLField()),
                ('url', models.SlugField(max_length=60, verbose_name='Ссылка')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('created_date', models.DateTimeField(verbose_name='Дата')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Имя ползователя')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Article',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='GroupArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Group name')),
                ('description', models.TextField(verbose_name='Group description')),
                ('private', models.BooleanField(default=False, verbose_name='Private goup?')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Url to group')),
                ('created_date', models.DateTimeField(verbose_name='Group created date')),
                ('articles', models.ManyToManyField(to='main.Article', verbose_name='Articles')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Group author')),
            ],
            options={
                'verbose_name': 'Group Article',
                'verbose_name_plural': 'Group Articles',
            },
        ),
    ]