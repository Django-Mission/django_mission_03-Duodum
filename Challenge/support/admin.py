from django.contrib import admin
from .models import Faq, Inquiry, Answer

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_category', 'updated_at')
    list_filter = ('question_category',)
    search_fields = ('question',)
    search_help_text = '제목 검색'
    readonly_fields = ('created_at', 'updated_at')

class AnswerInlines(admin.TabularInline):
    model = Answer
    extra = 1
    min_num = 0
    max_num = 1
    verbose_name = '답변'
    verbose_name_plural = '답변'
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('state_category', 'title', 'title_category', 'created_at', 'generators')
    list_filter = ('state_category', 'title_category')
    search_fields = ('title', 'email', 'phone', 'generators__username', 'generators__email')
    search_help_text = '제목, 이메일, 전화번호 검색'
    readonly_fields = ('created_at', 'updated_at')

    inlines = [AnswerInlines]

    actions = ['send_Info']

    def send_Info(modeladmin, request, queryset):
        for item in queryset:
            if item.email_checkbox and item.phone_checkbox:
                print(f'이메일 : {item.email}\n전화번호 : {item.phone}')
            else:
                pass