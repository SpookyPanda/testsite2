from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	publish_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.pubish_date = timezone.now()
		self.save()

	def valid_comment(self):
		return self.comments.filter(approved_comment=True)

	def get_absolute_url(self):
		return reverse("post_detail", kwargs={'pk':self.pk})


	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey('blog.Post', related_name = 'comments', on_delete=models.CASCADE)
	author = models.CharField(max_length = 127)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	approved_comment = 	models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse("post_details")

	def __str__(self):
		return self.text


