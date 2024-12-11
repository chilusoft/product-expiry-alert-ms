from django.db import models
from djangondor.models import BaseTimestampModel, NULLABLE, NULLABLE_CHARFIELD
from django.db.models import (
    CharField,
    IntegerField,
    FloatField,
    ForeignKey,
    ImageField,
    DateField,
    DateTimeField,
    BooleanField,
    ManyToManyField
)


class Product(BaseTimestampModel):
    name=CharField(**NULLABLE_CHARFIELD)
    image=ImageField(upload_to='products/images/%y/%m/%d', default='products/images/')
    batch=ForeignKey('ProductBatch', on_delete=models.CASCADE)
    product_category=ManyToManyField('ProductCategory')

    def __str__(self):
        return f'{self.name} --> {self.batch_id}'
    
class ProductCategory(BaseTimestampModel):
    name=CharField(**NULLABLE_CHARFIELD)
    image=ImageField(upload_to='products/assets/category/%y/%m/%d',default='products/assets/category/default.png')
class ProductBatch(BaseTimestampModel):
    batch_id=IntegerField(null=True,blank=True)
    expiry_date=DateField(null=True,blank=True)
    is_expired=BooleanField(default=False)
    quantity=models.BigIntegerField(default=0)
    supplier=ForeignKey('Supplier',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.batch_id} is Expired: {self.is_expired}'


class Supplier(BaseTimestampModel):
    store_name = models.CharField(max_length=255)
    store_location = models.CharField(**NULLABLE_CHARFIELD)
    store_capacity = models.IntegerField(default=0)
    store_type = models.CharField(**NULLABLE_CHARFIELD)

    def _str_(self):
        return self.store_name


class ScheduleQueue(BaseTimestampModel):
    batch = models.OneToOneField(ProductBatch, on_delete=models.CASCADE, related_name="schedule_queue")
    is_scheduled = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_notification_sent = models.BooleanField(default=False)
    recipient_emails = models.ManyToManyField('index.User', related_name="scheduled_notifications")

    def _str_(self):
        return f"Schedule Queue for {self.expiration_data.product.product_name}"



