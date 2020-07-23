from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3			# show this many choice inputs
# 

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 								{'fields': ['question_text']}),
		('Date Information', 	{'fields': ['pub_date'], 'classes': ['collapse']})
	]
	inlines = [ChoiceInline]
# 

admin.site.register(Question, QuestionAdmin)