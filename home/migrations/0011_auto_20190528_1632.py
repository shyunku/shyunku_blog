# Generated by Django 2.2.1 on 2019-05-28 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190528_1620'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.User_Info'),
        ),
    ]
