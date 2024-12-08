from django.db import models
from djangondor.models import BaseTimestampModel, NULLABLE, NULLABLE_CHARFIELD
from django.db.models import (
    CharField,
    IntegerField,
    FloatField,
    ForeignKey,
    ImageField,
    DateField
)


class Product(BaseTimestampModel):
    name=CharField(**NULLABLE_CHARFIELD)
    image=ImageField(upload_to='products/images/%y/%m/%d', default='products/images/')
    batch_id=ForeignKey('ProductBatch', on_delete=models.CASCADE)

class ProductBatch(BaseTimestampModel):
    batch_id=IntegerField(null=True,blank=True)
    expiry_date=DateField(null=True,blank=True)
    quantity=models.BigIntegerField(default=0)


