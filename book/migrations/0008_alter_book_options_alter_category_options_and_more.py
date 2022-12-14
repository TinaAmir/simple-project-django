# Generated by Django 4.1 on 2022-11-02 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'کتاب', 'verbose_name_plural': 'کتاب ها'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'زیر دسته', 'verbose_name_plural': 'زیر دسته ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on'], 'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'ارتباط', 'verbose_name_plural': 'ارتباطات'},
        ),
        migrations.AlterModelOptions(
            name='parentcategory',
            options={'verbose_name': 'دسته اصلی', 'verbose_name_plural': 'دسته های اصلی'},
        ),
        migrations.AlterModelOptions(
            name='writer',
            options={'verbose_name': 'نویسنده', 'verbose_name_plural': 'نویسندگان'},
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.category', verbose_name='زیر دسته'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='book_cover/', verbose_name='کاور'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='book',
            name='parent_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.parentcategory', verbose_name='دسته اصلی'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='book',
            name='show',
            field=models.BooleanField(default=True, verbose_name='نمایش'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=128, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='book',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.writer', verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=120, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.parentcategory', verbose_name='دسته اصلی'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book', verbose_name='کتاب'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=2000, verbose_name='نظر'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='نوشته شده در'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=100, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=500, null=True, verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=120, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=120, null=True, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='parentcategory',
            name='name',
            field=models.CharField(max_length=120, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='bio',
            field=models.TextField(max_length=1000, verbose_name='بیوگرافی'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='name',
            field=models.CharField(max_length=120, verbose_name='عنوان'),
        ),
    ]
