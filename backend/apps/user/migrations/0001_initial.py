# Generated by Django 3.2.8 on 2022-05-09 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('fullname', models.CharField(default='u_2022050918', max_length=50, verbose_name='Аты жөн')),
                ('password', models.CharField(max_length=254, verbose_name='Құпия сөз')),
                ('role', models.CharField(choices=[('site admin', 'Сайт әкімшісі'), ('org manager', 'Ұйым меңгеруші'), ('tenant', 'Жалға алушы')], max_length=20, verbose_name='Рөл')),
                ('gender', models.BooleanField(verbose_name='Жыныс')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Тіркелген уақыт')),
            ],
            options={
                'verbose_name': 'Пайдаланушы',
                'verbose_name_plural': 'Пайдаланушылар',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=254, verbose_name='Мазмұны')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Жіберілген уақыт')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to='user.user', verbose_name='Алушы')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to='user.user', verbose_name='Жіберуші')),
            ],
            options={
                'verbose_name': 'Хабарландыру',
                'verbose_name_plural': 'Хабарландырулар',
                'db_table': 'notification',
            },
        ),
    ]