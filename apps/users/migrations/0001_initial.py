# Generated by Django 2.1.1 on 2018-09-08 18:04

import utils.storage
import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='姓名')),
                ('gender', models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], max_length=6, null=True, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生年月')),
                ('icon', models.ImageField(blank=True, default='user_icon/defaultUserIcon.png', max_length=256, null=True, storage=utils.storage.ImageStorage(), upload_to='user_icon', verbose_name='头像')),
                ('institution', models.CharField(blank=True, max_length=255, null=True, verbose_name='所在院校')),
                ('computer_major', models.BooleanField(default=True, verbose_name='是否计算机专业')),
                ('graduate', models.BooleanField(default=False, verbose_name='是否毕业')),
                ('education', models.CharField(blank=True, max_length=255, null=True, verbose_name='学历')),
                ('signature', models.TextField(blank=True, max_length=255, null=True, verbose_name='个性签名')),
                ('mobile', models.CharField(blank=True, help_text='联系电话', max_length=11, null=True, verbose_name='电话')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('index', models.IntegerField(verbose_name='唯一标志')),
                ('name', models.CharField(max_length=30, verbose_name='角色名称')),
            ],
            options={
                'verbose_name': '用户角色',
                'verbose_name_plural': '用户角色',
                'ordering': ['-index'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('code', models.CharField(max_length=5, verbose_name='邀请码')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='编辑保存触发产生新邀请码', verbose_name='邀请码添加时间')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
            },
        ),
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=10, verbose_name='验证码')),
                ('mobile', models.CharField(max_length=11, verbose_name='电话')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '短信验证',
                'verbose_name_plural': '短信验证',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(to='users.Role', verbose_name='角色'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='teams',
            field=models.ManyToManyField(to='users.Team', verbose_name='所在班级'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
