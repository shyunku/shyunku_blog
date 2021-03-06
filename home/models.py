from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields

from django.urls import reverse



class User_Info(models.Model):
    user_id = models.CharField(max_length=20)
    user_nickname = models.CharField(max_length=25)
    user_pw = models.CharField(max_length=15)

    def __str__(self):
        return self.user_id


class Variables(models.Model):
    doc_index_recent = models.IntegerField(default=0)
    comment_index_recent = models.IntegerField(default=0)

    visits = models.IntegerField(default=0)
    visits_free = models.IntegerField(default=0)
    visits_rout = models.IntegerField(default=0)
    visits_lol = models.IntegerField(default=0)
    visits_dl = models.IntegerField(default=0)
    visits_web = models.IntegerField(default=0)
    visits_java = models.IntegerField(default=0)
    visits_window = models.IntegerField(default=0)
    visits_indiv = models.IntegerField(default=0)

    def __str__(self):
        return "Variables"


class Documents_Info(models.Model):
    def get_absolute_url(self):
        return reverse(
            'home:view_post', args={
                'pindex':self.doc_index,
                'classify':self.classify
            }
        )

    classify = models.CharField(max_length=20)
    doc_index = models.CharField(default="00001", max_length=15)
    doc_title = models.CharField(max_length=20)
    doc_writer = models.CharField(default="shyunku", max_length=20)
    doc_content = models.TextField(default="")
    doc_time = models.DateTimeField(auto_now_add=True, blank=True)
    doc_view_cnt = models.IntegerField(default=0)

    def __str__(self):
        return self.classify + "-" + self.doc_index + "-" + self.doc_writer + "-" + self.doc_title


class Comment(models.Model):
    comment_time = models.DateTimeField(auto_now_add=True, blank=True)
    comment_content = models.TextField(default="")
    comment_writer = models.ForeignKey(User_Info, null=True, on_delete=models.CASCADE)
    comment_post = models.ForeignKey(Documents_Info, null=True, on_delete=models.CASCADE, related_name="commented")
    comment_id = models.CharField(default="000001", max_length=15)

    def __str__(self):
        return self.comment_post.__str__() + "-" + self.comment_writer.user_nickname


class SummerNote(summer_model.Attachment):
    summer_field = summer_fields.SummernoteTextField(default='')


