from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class choiceInLine(admin.TabularInline):    #admin.StackedInLine
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Data information', {'fields': ['pub_date']}),
    ]
    inlines = [choiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)