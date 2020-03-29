# Generated by Django 3.0.3 on 2020-03-29 06:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_date', models.DateTimeField(auto_now=True)),
                ('day_of_the_week', models.IntegerField()),
                ('court_number', models.IntegerField()),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('court_count', models.IntegerField()),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=200, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Racket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rackets', to='api.Court')),
            ],
        ),
        migrations.CreateModel(
            name='Shuttlecock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('count_per_unit', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('remaining', models.IntegerField()),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shuttlecocks', to='api.Court')),
            ],
        ),
        migrations.CreateModel(
            name='ShuttlecockBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve_date', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shuttlecock_bookings', to='api.Booking')),
                ('shuttlecock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shuttlecock_bookings', to='api.Shuttlecock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shuttlecock_bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RacketBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve_date', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('day_of_the_week', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)])),
                ('start', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(47)])),
                ('end', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(47)])),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='racket_bookings', to='api.Booking')),
                ('racket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='racket_bookings', to='api.Racket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='racket_bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.Court')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='court',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='api.Court'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_the_week', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('status', models.BigIntegerField(default=0)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('court_number', models.IntegerField(blank=True)),
                ('court', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='api.Court')),
                ('racket', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='api.Racket')),
            ],
            options={
                'unique_together': {('court', 'court_number', 'day_of_the_week')},
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('review', models.CharField(max_length=200)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.Court')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'court')},
            },
        ),
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('credit', models.IntegerField(blank=True, default=0)),
                ('phone_number', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(regex='^0\\d{8,9}$')])),
                ('ban_list', models.ManyToManyField(blank=True, related_name='banned', to=settings.AUTH_USER_MODEL)),
                ('base_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extended', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('base_user',)},
            },
        ),
    ]
