#!encoding:utf-8
from __future__ import unicode_literals

from django.core.validators import MinValueValidator

from users.models import *


def upload_to(instance, fielname):
	return os.path.join("goods", str(instance.id), fielname)


class Goods(BaseModelMixin):
	"""商品"""

	GTYPE = (
		("1", "实体商品"),
		("2", "虚拟商品"),
	)

	name = models.CharField('商品名称', max_length=256)
	gtype = models.CharField('商品类型', max_length=1, choices=GTYPE)
	style = models.CharField('款式', max_length=50, default="", blank=True)
	images = models.ImageField('商品图片', upload_to=upload_to, storage=ImageStorage())
	integral = models.PositiveIntegerField("积分", validators=[MinValueValidator(1)])
	stock = models.PositiveIntegerField("库存", default=0)
	residue_stock = models.PositiveIntegerField("剩余库存", default=0)
	detail = models.TextField(verbose_name="商品详情", default="")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "商品"
		verbose_name_plural = verbose_name


class ExchangeRecords(BaseModelMixin):
	"""积分兑换记录"""

	user = models.ForeignKey(UserProfile, verbose_name="兑换用户", related_name="ExchangeRecords",
									on_delete=models.CASCADE)
	goods = models.ForeignKey(Goods, verbose_name="兑换商品", on_delete=models.CASCADE)
	ship = models.BooleanField('是否发货', default=False)
	ship_time = models.DateTimeField(verbose_name='发货时间', auto_now=True)

	def __str__(self):
		return self.user.name + "|" + self.goods.name

	class Meta:
		verbose_name = "兑换记录"
		verbose_name_plural = verbose_name
