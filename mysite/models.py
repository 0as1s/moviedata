# encoding=utf-8
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

# Index(['序号', '发行年份', '上映时间', '地区', '片名（日语）', '片名（中文）', '导演', '类型', '发行方',
#        '媒体评分', 'Filmarks观众总评分', 'Filmarks观众评分人数', 'Yahoo观众总评分', 'Yahoo观众评分人数',
#        'Yahoo故事评分', 'Yahoo人物评分', 'Yahoo表演评分', 'Yahoo画面评分', 'Yahoo音乐评分', '票房',
#        '观影人数', '备注（例如获奖', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24',
#        'Unnamed: 25'],
#       dtype='object')


class Movie(models.Model):
    festival = models.CharField(verbose_name="电影节一", null=True, max_length=1000)
    festival2 = models.CharField(verbose_name="电影节二", null=True, max_length=1000)
    publish_year = models.CharField(verbose_name="发行年份", null=True, max_length=1000)
    publish_date = models.CharField(verbose_name="上映时间", null=True, max_length=1000)
    region = models.CharField(verbose_name="地区", max_length=100, null=True)
    title_original = models.CharField(verbose_name="外文名", max_length=1000)
    title_translated = models.CharField(verbose_name="中文名", max_length=1000)
    director = models.CharField(verbose_name="导演", max_length=1000, null=True)
    topic = models.CharField(verbose_name="类型", max_length=1000, null=True)
    producer = models.CharField(verbose_name="出品方", max_length=1000, null=True)
    publisher = models.CharField(verbose_name="发行方", max_length=1000, null=True)
    media_score = models.FloatField(verbose_name="媒体评分", null=True)
    people_score = models.FloatField(verbose_name="观众评分", null=True)
    people_score_count = models.FloatField(verbose_name="观众评分人数", null=True)
    filmarks_score = models.FloatField(verbose_name="Filmarks观众总评分", null=True)
    filmarks_score_count = models.IntegerField(verbose_name="Filmarks观众评分人数", null=True)
    yahoo_score = models.FloatField(verbose_name="Yahoo观众总评分", null=True)
    yahoo_score_count = models.FloatField(verbose_name="Yahoo观众评分人数", null=True)
    yahoo_story_score = models.FloatField(verbose_name="Yahoo故事评分", null=True)
    yahoo_character_score = models.FloatField(verbose_name="Yahoo人物评分", null=True)
    yahoo_act_score = models.FloatField(verbose_name="Yahoo表演评分", null=True)
    yahoo_image_score = models.FloatField(verbose_name="Yahoo画面评分", null=True)
    yahoo_music_score = models.FloatField(verbose_name="Yahoo音乐评分", null=True)
    sells = models.FloatField(verbose_name="票房", null=True)
    count = models.IntegerField(verbose_name="观影人数", null=True)
    source = models.CharField(max_length=1000, verbose_name="来源", null=True)
    comment = models.CharField(max_length=1000, verbose_name="备注", null=True)
    format = models.CharField(max_length=100, verbose_name="上映形式", null=True)
    type_of_festival = models.CharField(max_length=100, verbose_name="电影节性质", null=True)
    file = models.CharField(max_length=100, verbose_name="原始文件", null=True)

