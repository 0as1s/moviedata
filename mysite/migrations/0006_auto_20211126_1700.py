# Generated by Django 3.2.9 on 2021-11-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_alter_movie_publish_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='festival',
            field=models.CharField(max_length=1000, null=True, verbose_name='电影节一'),
        ),
        migrations.AddField(
            model_name='movie',
            name='festival2',
            field=models.CharField(max_length=1000, null=True, verbose_name='电影节二'),
        ),
        migrations.AddField(
            model_name='movie',
            name='file',
            field=models.CharField(max_length=100, null=True, verbose_name='原始文件'),
        ),
        migrations.AddField(
            model_name='movie',
            name='format',
            field=models.CharField(max_length=100, null=True, verbose_name='上映形式'),
        ),
        migrations.AddField(
            model_name='movie',
            name='people_score',
            field=models.FloatField(null=True, verbose_name='观众评分'),
        ),
        migrations.AddField(
            model_name='movie',
            name='people_score_count',
            field=models.FloatField(null=True, verbose_name='观众评分人数'),
        ),
        migrations.AddField(
            model_name='movie',
            name='producer',
            field=models.CharField(max_length=1000, null=True, verbose_name='出品方'),
        ),
        migrations.AddField(
            model_name='movie',
            name='source',
            field=models.CharField(max_length=1000, null=True, verbose_name='来源'),
        ),
        migrations.AddField(
            model_name='movie',
            name='type_of_festival',
            field=models.CharField(max_length=100, null=True, verbose_name='电影节性质'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='comment',
            field=models.CharField(max_length=1000, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=1000, null=True, verbose_name='导演'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='publish_date',
            field=models.CharField(max_length=1000, null=True, verbose_name='上映时间'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='publish_year',
            field=models.CharField(max_length=1000, null=True, verbose_name='发行年份'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='publisher',
            field=models.CharField(max_length=1000, null=True, verbose_name='发行方'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title_original',
            field=models.CharField(max_length=1000, verbose_name='外文名'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title_translated',
            field=models.CharField(max_length=1000, verbose_name='中文名'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='topic',
            field=models.CharField(max_length=1000, null=True, verbose_name='类型'),
        ),
    ]