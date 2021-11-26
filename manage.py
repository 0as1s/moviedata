#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import pandas as pd
import numpy as np
import django


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


#'序号', '发行年份', '上映时间', '地区', '片名（日语）', '片名（中文）', '导演', '类型', '发行方',
#       '媒体评分', '观众评分', '票房', '观影人数', '备注（例如获奖'


def process_df(df, name):
    df = df.replace({np.nan: None})

    from mysite.models import Movie
    from django.db.models import IntegerField, FloatField

    verbose = {field.verbose_name: field.name for field in Movie._meta.get_fields()}
    verbose_type = {field.verbose_name: field for field in Movie._meta.get_fields()}

    for index, row in df.iterrows():
        object_dict = dict()
        for k in verbose:
            if k not in row:
                continue
            try:
                if isinstance(verbose_type[k], IntegerField):
                    if row[k] is not None:
                        object_dict[verbose[k]] = int(row[k])
                elif isinstance(verbose_type[k], FloatField):
                    if row[k] is not None:
                        object_dict[verbose[k]] = float(row[k])
                else:
                    if row[k] is not None:
                        object_dict[verbose[k]] = row[k]
            except ValueError:
                continue
        object_dict["file"] = name
        movie = Movie(**object_dict)
        try:
            movie.save()
        except django.db.utils.DataError:
            continue


def init():
    #from mysite.models import Movie
    #Movie.objects.all().delete()
    files = os.listdir("data")
    for f in files:
        if not f.endswith("xlsx"):
            continue
        sheet = 0
        while True:
            try:
                df = pd.read_excel(os.path.join("data", f), sheet_name=sheet)
                process_df(df, f)
                sheet += 1
            except IndexError:
                break


if __name__ == '__main__':
    main()
    #init()
