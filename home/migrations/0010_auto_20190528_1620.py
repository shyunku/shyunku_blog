# Generated by Django 2.2.1 on 2019-05-28 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190528_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_id',
            field=models.CharField(default='000001', max_length=15),
        ),
        migrations.AddField(
            model_name='variables',
            name='comment_index_recent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.User_Info'),
        ),
        migrations.AlterField(
            model_name='variables',
            name='doc_index_recent',
            field=models.IntegerField(default=0),
        ),
    ]
