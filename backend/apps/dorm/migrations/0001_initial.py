# Generated by Django 3.2.8 on 2022-05-09 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=24, null=True, verbose_name='Төсек орын атауы')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Сипаттама')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Құрылған уақыт')),
                ('owner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user', verbose_name='Иесі (Пайдаланушы)')),
            ],
            options={
                'verbose_name': 'Төсек орын',
                'verbose_name_plural': 'Төсек орындар',
                'db_table': 'bed',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='Қала атуы')),
            ],
            options={
                'verbose_name': 'Қала',
                'verbose_name_plural': 'Қалалар',
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Dorm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Жатақхана атуы')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Сипаттама')),
                ('address', models.CharField(max_length=60, verbose_name='Жатақхана нақты мекен-жайы')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Құрылған уақыт')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.city', verbose_name='Орналасқан қала')),
            ],
            options={
                'verbose_name': 'Жатақхана',
                'verbose_name_plural': 'Жатақханалар',
                'db_table': 'dorm',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='Бөлме атауы')),
                ('floor', models.PositiveSmallIntegerField(verbose_name='Қабат нөмері')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Сипаттама')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Құрылған уақыт')),
                ('dorm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.dorm', verbose_name='Жатақхана')),
            ],
            options={
                'verbose_name': 'Бөлме',
                'verbose_name_plural': 'Бөлмелер',
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/dorm/room_image/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.room', verbose_name='Бөлме')),
            ],
            options={
                'verbose_name': 'Бөлме суреті',
                'verbose_name_plural': 'Бөлме суреттері',
                'db_table': 'room_image',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Ұйым атуы')),
                ('category', models.CharField(choices=[('university', 'Университет'), ('college', 'Колледж'), ('school', 'Мектеп'), ('other', 'Басқа')], max_length=10, verbose_name='Санат')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Құрылған уақыт')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='Құрушы')),
            ],
            options={
                'verbose_name': 'Ұйым',
                'verbose_name_plural': 'Ұйымдар',
                'db_table': 'organization',
            },
        ),
        migrations.CreateModel(
            name='DormImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/dorm/dorm_image/')),
                ('dorm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.dorm', verbose_name='Жатақхана')),
            ],
            options={
                'verbose_name': 'Жатақхана суреті',
                'verbose_name_plural': 'Жатақхана суреттері',
                'db_table': 'dorm_image',
            },
        ),
        migrations.AddField(
            model_name='dorm',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.organization', verbose_name='Ұйым'),
        ),
        migrations.CreateModel(
            name='BedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/dorm/bed_image/')),
                ('bed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.bed', verbose_name='Төсек орын')),
            ],
            options={
                'verbose_name': 'Төсек орын суреті',
                'verbose_name_plural': 'Төсек орын суреттері',
                'db_table': 'bed_image',
            },
        ),
        migrations.AddField(
            model_name='bed',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.room', verbose_name='Бөлме'),
        ),
    ]
