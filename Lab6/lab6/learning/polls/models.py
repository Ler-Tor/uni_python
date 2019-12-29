from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	comment = models.CharField(max_length=10)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text

class Choice(models.Model):

	on_delete = models.DO_NOTHING
	question = models.ForeignKey(Question, on_delete = models.PROTECT)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

