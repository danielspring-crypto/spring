from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=255)
	caption = models.TextField()
	image_type = models.CharField(max_length=255)
	image = models.ImageField(default='default.jpg', upload_to='post')
	date_posted = models.DateTimeField("date published")

	def __str__(self):
		return self.title