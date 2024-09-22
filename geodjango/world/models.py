from django.contrib.gis.db import models

"""
WorldBorderモデルはshpファイルの構造を見て手動で作成したが、ogrinspectコマンド使えばモデルの作成とLayerMapping用のdict生成を自動化できる。

コマンド
python manage.py ogrinspect world/data/TM_WORLD_BORDERS-0.3.shp WorldBorder --srid=4326 --mapping --multi
"""


class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField("Population 2005")
    pop2005 = models.IntegerField("Population 2005")
    fips = models.CharField("FIPS Code", max_length=2, null=True)
    iso2 = models.CharField("2 Digit ISO", max_length=2)
    iso3 = models.CharField("3 Digit ISO", max_length=3)
    un = models.IntegerField("United Nations Code")
    region = models.IntegerField("Region Code")
    subregion = models.IntegerField("Sub-Region Code")
    lon = models.FloatField()
    lat = models.FloatField()

    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name
