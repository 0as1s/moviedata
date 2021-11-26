from django.contrib import admin
from mysite.models import Person, Movie

# class Movie(models.Model):
#     publish_year = models.IntegerField(verbose_name="发行年份")
#     publish_date = models.DateField(verbose_name="日期")
#     region = models.CharField(verbose_name="地区", max_length=100)
#     title_original = models.CharField(verbose_name="电影名", max_length=100)
#     title_translated = models.CharField(verbose_name="电影名（中文）", max_length=100)
#     director = models.CharField(verbose_name="导演", max_length=100)
#     topic = models.CharField(verbose_name="类型", max_length=100)
#     publisher = models.CharField(verbose_name="发行方", max_length=100)
#     media_score = models.FloatField(verbose_name="媒体评分")
#     filmarks_score = models.FloatField(verbose_name="filmarks观众评分")
#     yahoo_act_score = models.FloatField(verbose_name="yahoo表演评分")
#     yahoo_image_score = models.FloatField(verbose_name="雅虎画面评分")
#     yahoo_music_score = models.FloatField(verbose_name="雅虎音乐评分")
#     sells = models.FloatField(verbose_name="票房")
#     count = models.IntegerField(verbose_name="观影人数")
#     comment = models.CharField(max_length=1000, verbose_name="备注")


class MovieAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in Movie._meta.get_fields()]
    list_display = [field.name for field in Movie._meta.get_fields()]
    list_filter = ("file", "type_of_festival",)


    class Media:
        css = {
            'all': ('fancy.css',)
        }


admin.site.register(Movie, MovieAdmin)
