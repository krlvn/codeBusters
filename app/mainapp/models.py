from django.db import models
from django.conf import settings

from ckeditor.fields import RichTextField
from django.urls import reverse


class NotDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Category(models.Model):
    # Модель категорий

    name = models.CharField(max_length=45, verbose_name="наименование", unique=True)
    description = models.CharField(max_length=300, blank=True, verbose_name="описание")
    alias = models.SlugField(max_length=50, unique=True, verbose_name="Alias")
    active = models.BooleanField(default=True, verbose_name="активна")
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}{"" if self.active else "(блок)"}'

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def get_absolute_url(self):
        return reverse("alias", kwargs={"menu": self.alias})


class Status(models.Model):
    # Модель статусы статьи
    name = models.CharField(
        max_length=45, verbose_name="наименование статуса", unique=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Статус статьи"
        verbose_name_plural = "Статусы статей"


class Post(models.Model):
    # Модель статьей
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name="Заголовок статьи", max_length=110, unique=False
    )
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(
        Category, verbose_name="Категории статей", on_delete=models.CASCADE
    )
    active = models.BooleanField(verbose_name="активна", default=False, db_index=True)
    is_deleted = models.BooleanField(
        verbose_name="Удалена", default=False, db_index=True
    )
    # status = models.ForeignKey(Status, verbose_name='Статусы статьи', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        null=True,
        verbose_name="Главное изображение статьи",
        upload_to="post_image",
        blank=True,
        max_length=150,
    )
    content = RichTextField(null=True, blank=True)
    objects_all = models.Manager()
    objects = NotDeletedManager()

    def __str__(self):
        return f'{self.title}{"" if self.active else "(блок)"}'

    def delete(self):
        self.is_deleted = True
        self.save()

    @property
    def likes_count(self):
        return self.post_likes.filter(status=True, active=True).count()

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"


class Comment(models.Model):
    # Модель комментариев
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        "self",
        verbose_name="Родитель",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    post = models.ForeignKey(
        Post,
        related_name="comments",
        verbose_name="Название статьи",
        on_delete=models.CASCADE,
    )
    text = models.TextField(verbose_name="Комментарий")
    active = models.BooleanField(verbose_name="активна", default=False, db_index=True)
    is_deleted = models.BooleanField(
        verbose_name="Удалена", default=False, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects_all = models.Manager()
    objects = NotDeletedManager()

    def __str__(self):
        return f"{self.post}"

    def delete(self):
        self.is_deleted = True
        self.save()

    @property
    def likes_count(self):
        return self.comment_likes.filter(status=True, active=True).count()

    class Meta:
        verbose_name = "коментарий"
        verbose_name_plural = "коментарии"


class CommentLikes(models.Model):
    comment = models.ForeignKey(
        Comment,
        verbose_name="Название статьи",
        related_name="comment_likes",
        on_delete=models.CASCADE,
    )
    status = models.BooleanField(default=True, verbose_name="Статус")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Автор",
        related_name="comment_likes",
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(verbose_name="активна", default=True, db_index=True)

    class Meta:
        verbose_name = "Лайк к коментарию"
        verbose_name_plural = "Лайки к коментариям"
        unique_together = ("comment_id", "user_id")


class PostLikes(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="Название статьи",
        related_name="post_likes",
        on_delete=models.CASCADE,
    )
    status = models.BooleanField(default=True, verbose_name="Статус")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Автор",
        related_name="post_likes",
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(verbose_name="активна", default=True, db_index=True)

    class Meta:
        verbose_name = "Лайк к статье"
        verbose_name_plural = "Лайки к статьям"
        unique_together = ("post_id", "user_id")
