# Generated by Django 3.2.9 on 2021-11-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20211120_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='filmarks_score_count',
            field=models.IntegerField(null=True, verbose_name='Filmarks观众评分人数'),
        ),
        migrations.AddField(
            model_name='movie',
            name='yahoo_character_score',
            field=models.FloatField(null=True, verbose_name='Yahoo人物评分'),
        ),
        migrations.AddField(
            model_name='movie',
            name='yahoo_score',
            field=models.FloatField(null=True, verbose_name='Yahoo观众总评分'),
        ),
        migrations.AddField(
            model_name='movie',
            name='yahoo_score_count',
            field=models.FloatField(null=True, verbose_name='Yahoo观众评分人数'),
        ),
        migrations.AddField(
            model_name='movie',
            name='yahoo_story_score',
            field=models.FloatField(null=True, verbose_name='Yahoo故事评分'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='comment',
            field=models.CharField(max_length=1000, null=True, verbose_name='备注（例如获奖'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='filmarks_score',
            field=models.FloatField(null=True, verbose_name='Filmarks观众总评分'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='publish_date',
            field=models.CharField(max_length=100, null=True, verbose_name='上映时间'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title_original',
            field=models.CharField(max_length=100, verbose_name='片名（日语）'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title_translated',
            field=models.CharField(max_length=100, verbose_name='片名（中文）'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='yahoo_act_score',
            field=models.FloatField(null=True, verbose_name='Yahoo表演评分'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='yahoo_image_score',
            field=models.FloatField(null=True, verbose_name='Yahoo画面评分'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='yahoo_music_score',
            field=models.FloatField(null=True, verbose_name='Yahoo音乐评分'),
        ),
    ]