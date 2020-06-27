from django.contrib import admin
from .models import Question, Answer, UserRespond


# class AnswerInline(admin.StackedInline)
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'is_active')

    fieldsets = [
        (None,
         {'fields': ['title', 'is_active']}
         ),
        ('Информация о дате',
         {'fields': ['date_published'],
          'classes': ['collapse']}
         ),
    ]
    inlines = [AnswerInline]
    list_filter = ['date_published']
    date_hierarchy = 'date_published'


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(UserRespond)




