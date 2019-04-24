from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = "分类"  # 类的复数


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = "标签"  # 类的复数


class Blog(models.Model):
    """
    id，标题，摘要，内容，作者，发布时间，修改时间，
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField('标题', max_length=125)  # 标题
    author = models.CharField('作者', max_length=100)  # 作者
    tags = models.ManyToManyField(Tag, verbose_name='标签', max_length=100, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类', max_length=100, blank=True)
    summary = RichTextUploadingField('摘要')  # 摘要
    content = RichTextUploadingField('正文')  # 正文
    views = models.IntegerField('阅读量', default=0)  # 阅读量
    create_at = models.DateTimeField('发布时间')  # 发布时间
    update_at = models.DateTimeField('更新时间')  # 更新时间
    topped = models.BooleanField('置顶', default=False)  # 是否置顶

    def __str__(self):
        return self.title   # 后台显示标题

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:details', args=[self.title])

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = "文章"  # 类的复数
        ordering = ['-update_at']


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    mid = models.ForeignKey(Blog, verbose_name='被评论文章')
    name = models.CharField('姓名', max_length=100)
    email = models.EmailField('邮箱', max_length=100)
    message = models.TextField('留言')
    create_at = models.DateTimeField('评论时间', auto_now_add=True)  # 评论时间

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'


class FriendlyLink(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('标题', max_length=30)
    url = models.URLField('链接')
    message = models.TextField('备注', blank=True)
    create_at = models.DateTimeField('添加时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'


class Siteinfo(models.Model):
    title = models.CharField('网站标题', max_length=30)
    icon = models.ImageField('网站图标', upload_to='icon')
    pagesnum = models.IntegerField('一页文章数', default=8)

    class Meta:
        verbose_name = '网站信息'
        verbose_name_plural = '网站信息'


class Adsense(models.Model):
    img = models.ImageField('推广图片', upload_to='tu')
    title = models.TextField('推广文案', blank=True)
    url = models.URLField('推广链接')

    class Meta:
        verbose_name = '推广素材'
        verbose_name_plural = '推广素材'

