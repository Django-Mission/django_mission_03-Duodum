from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Faq(models.Model):
    GENERAL = 'GE'
    ACCOUNT = 'AC'
    ETC = 'ET'

    CATEGORY_CHOICES = [
        (GENERAL, '일반'),
        (ACCOUNT, '계정'),
        (ETC, '기타'),
    ]

    question = models.CharField(
        '제목',
        max_length=100,
    )

    question_category = models.CharField(
        '카테고리',
        max_length = 2,
        choices = CATEGORY_CHOICES,
        default = GENERAL,
    )

    answer = models.TextField('답변')
    generators = models.ForeignKey(User, models.CASCADE, related_name='generators_faq')
    created_at = models.DateTimeField('생성일시', auto_now_add=True)
    last_modifier = models.ForeignKey(User, models.CASCADE, null=True, blank=True, related_name='last_modifier_faq')
    updated_at = models.DateTimeField('수정일시', auto_now=True)

class Inquiry(models.Model):
    GENERAL = 'GE'
    ACCOUNT = 'AC'
    ETC = 'ET'

    CATEGORY_CHOICES = [
        (GENERAL, '일반'),
        (ACCOUNT, '계정'),
        (ETC, '기타'),
    ]

    title_category = models.CharField(
        '질문 카테고리',
        max_length = 10,
        choices = CATEGORY_CHOICES,
        default = GENERAL,
    )
    title = models.CharField(
        '제목',
        max_length=100,
    )

    e_mail = models.CharField(
        '이메일',
        max_length = 50,
    )
    e_mail_checkbox = models.BooleanField('이메일 수신 여부', default=False)

    phone = models.CharField(
        '전화번호',
        max_length=15,
    )
    phone_checkbox = models.BooleanField('문자 수신 여부', default=False)
    
    content = models.TextField('내용')
    image = models.ImageField('이미지', null=True, blank=True)
    generators = models.ForeignKey(User, models.CASCADE, related_name='generators_inquiry')
    created_at = models.DateTimeField('생성일시', auto_now_add=True)
    last_modifier = models.ForeignKey(User, models.CASCADE, null=True, blank=True, related_name='last_modifier_inquiry')
    updated_at = models.DateTimeField('수정일시', auto_now=True)

class Answer(models.Model):
    answer = models.TextField('답변 내용')
    inquiry = models.ForeignKey('Inquiry', models.CASCADE)
    generators = models.ForeignKey(User, models.CASCADE, related_name='generators_answer')
    created_at = models.DateTimeField('생성일시', auto_now_add=True)
    last_modifier = models.ForeignKey(User, models.CASCADE, null=True, blank=True, related_name='last_modifier_answer')
    updated_at = models.DateTimeField('수정일시', auto_now=True)