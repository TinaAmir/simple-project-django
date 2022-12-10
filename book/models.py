from django.db import models

# Create your models here.

class ParentCategory(models.Model):
    name = models.CharField(max_length=120,verbose_name="عنوان")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "دسته های اصلی"
        verbose_name = "دسته اصلی"
        
class Category(models.Model):
    name = models.CharField(max_length=120,verbose_name="عنوان")
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, null=True,verbose_name="دسته اصلی")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "زیر دسته ها"
        verbose_name = "زیر دسته"


class Writer(models.Model):
    name = models.CharField(max_length=120,verbose_name="عنوان")
    bio = models.TextField(max_length=1000,verbose_name="بیوگرافی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "نویسندگان"
        verbose_name = "نویسنده"
        
class Book(models.Model) :
    
    title = models.CharField(max_length=128,verbose_name="عنوان")
    description = models.TextField(max_length=1000,verbose_name="توضیحات")
    show = models.BooleanField(default=True,verbose_name="نمایش")
    publish_date = models.DateField(auto_now_add=True,verbose_name="تاریخ انتشار")
    cover = models.ImageField(upload_to="book_cover/" , null=True,verbose_name="کاور")
    price = models.IntegerField(default=0,verbose_name="قیمت")
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE , null=True,verbose_name="نویسنده")
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, null=True,verbose_name="دسته اصلی")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,verbose_name="زیر دسته")
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name_plural = "کتاب ها"
        verbose_name= "کتاب"
        
class Contact(models.Model):
    name = models.CharField(max_length=120,null=True,verbose_name= "نام")
    email = models.EmailField(null=True,verbose_name= "ایمیل")
    subject = models.CharField(max_length=120,null=True,verbose_name= "موضوع")
    message = models.TextField(max_length=500,null=True,verbose_name= "پیام")
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        verbose_name_plural = "ارتباطات"
        verbose_name= "ارتباط"
        
    
class Comment(models.Model):
    book = models.ForeignKey(Book , on_delete=models.CASCADE,verbose_name= "کتاب")
    user = models.CharField(max_length=100,verbose_name= "کاربر")
    comment = models.TextField(max_length=2000,verbose_name="نظر")
    created_on = models.DateTimeField(auto_now_add=True,verbose_name= "نوشته شده در")
    
    class Meta:
        ordering = ["created_on"]
        verbose_name_plural = "نظرات"
        verbose_name= "نظر"
        
    def __str__ (self):
        return self.comment
