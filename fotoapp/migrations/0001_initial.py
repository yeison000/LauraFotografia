# Generated by Django 2.2.12 on 2020-05-20 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albume_fields', models.ImageField(upload_to='static/imgenesportada')),
                ('nombre', models.CharField(max_length=70, null=True)),
                ('fecha', models.DateField()),
                ('comentario', models.CharField(max_length=500, null=True)),
                ('albumDestacado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '1) Album',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('telefono', models.IntegerField(null=True)),
                ('respuesta1', models.CharField(max_length=500, null=True)),
                ('respuesta2', models.CharField(max_length=500, null=True)),
                ('respuesta3', models.CharField(max_length=500, null=True)),
                ('respuesta4', models.CharField(max_length=500, null=True)),
                ('respuesta5', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': '5) Contacto',
            },
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
                ('pack_fields', models.ImageField(blank=True, upload_to='static/packs')),
                ('descripcion', models.TextField(blank=True, max_length=900, null=True)),
            ],
            options={
                'verbose_name': '4) Pack',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, null=True)),
                ('image', models.ImageField(upload_to='static/imagenPorfolio')),
            ],
            options={
                'verbose_name': '0) Portfolio',
            },
        ),
        migrations.CreateModel(
            name='PortfolioSoloImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, null=True)),
                ('image', models.ImageField(upload_to='static/imagenPorfolio')),
            ],
        ),
        migrations.CreateModel(
            name='SoloImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/imagenesalbum')),
            ],
            options={
                'verbose_name': '3) Beauty & Retouch',
            },
        ),
        migrations.CreateModel(
            name='ImgAlbume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/imagenesalbum')),
                ('fkAlbume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fotoapp.Albume')),
            ],
            options={
                'verbose_name': '2) Img de los Album',
            },
        ),
        migrations.AddField(
            model_name='albume',
            name='fkPortFolio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fotoapp.Portfolio'),
        ),
    ]
