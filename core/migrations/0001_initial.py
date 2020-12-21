# Generated by Django 3.1.4 on 2020-12-18 14:42

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_manager_sus', models.BooleanField(default=False, verbose_name='Manager SUS status')),
                ('is_professional_health', models.BooleanField(default=False, verbose_name='Professional health status')),
                ('is_patient', models.BooleanField(default=False, verbose_name='Patient status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('co_unidade', models.IntegerField(primary_key=True, serialize=False)),
                ('co_cnes', models.IntegerField()),
                ('nu_cnpj', models.CharField(blank=True, max_length=15)),
                ('no_razao_social', models.CharField(blank=True, max_length=255)),
                ('no_fantasia', models.CharField(blank=True, max_length=255)),
                ('nu_latitude', models.CharField(blank=True, default=0.0, max_length=50, null=True)),
                ('nu_longitude', models.CharField(blank=True, default=0.0, max_length=50, null=True)),
                ('no_logradouro', models.CharField(blank=True, max_length=255)),
                ('nu_endereco', models.CharField(blank=True, max_length=55)),
                ('no_complemento', models.CharField(blank=True, max_length=255)),
                ('no_bairro', models.CharField(blank=True, max_length=255)),
                ('co_cep', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('cod', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='User_Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(max_length=55)),
                ('date_application', models.DateField()),
                ('is_professional_created', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vaccine')),
            ],
        ),
        migrations.CreateModel(
            name='User_Estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vinculo', models.BooleanField(default=True)),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estabelecimento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('cod', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('cod_uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.uf')),
            ],
        ),
        migrations.AddField(
            model_name='estabelecimento',
            name='co_municipio_gestor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.municipio'),
        ),
    ]
