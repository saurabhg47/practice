from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_dt', 'question_test']
    # fieldsets = [(None, {'fields':['question_test']}),
    #              ('Date Information', {'fields': ['pub_dt'], 'classes': ['collapse']}),
    #             ]
    list_display = ('pub_dt', 'question_test', 'was_published_recently')
    list_filter = ['pub_dt']
    search_fields = ['question_test']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
