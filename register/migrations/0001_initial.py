# Generated by Django 2.2.7 on 2019-12-06 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cell_tech', models.CharField(max_length=100)),
                ('cell_manufacturer', models.CharField(max_length=100)),
                ('no_of_cells', models.CharField(max_length=100)),
                ('no_of_cells_in_series', models.CharField(max_length=100)),
                ('no_of_series_strings', models.CharField(max_length=100)),
                ('no_of_diodes', models.CharField(max_length=100)),
                ('length', models.CharField(max_length=100)),
                ('width', models.CharField(max_length=100)),
                ('superstate_type', models.CharField(max_length=100)),
                ('superstate_manufacturer', models.CharField(max_length=100)),
                ('substrate_type', models.CharField(max_length=100)),
                ('substrate_manufacturer', models.CharField(max_length=100)),
                ('frame_type', models.CharField(max_length=100)),
                ('frame_adhesive', models.CharField(max_length=100)),
                ('encapsulate_type', models.CharField(max_length=100)),
                ('encapsulate_manufacturer', models.CharField(max_length=100)),
                ('junction_box_type', models.CharField(max_length=100)),
                ('junction_box_manufacturer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('published_on', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('office_phone', models.CharField(max_length=100)),
                ('cell_phone', models.CharField(max_length=100)),
                ('prefix', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete='cascade', to='register.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('fl_required', models.CharField(max_length=100)),
                ('fl_frequency', models.CharField(max_length=100)),
                ('standard', models.ForeignKey(on_delete='DO_NOTHING', to='register.Standard')),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_voltage', models.CharField(max_length=100)),
                ('voc', models.CharField(max_length=100)),
                ('isc', models.CharField(max_length=100)),
                ('vmp', models.CharField(max_length=100)),
                ('imp', models.CharField(max_length=100)),
                ('pmp', models.CharField(max_length=100)),
                ('ff', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete='DO_NOTHING', to='register.Product')),
                ('sequence_id', models.ForeignKey(on_delete='DO_NOTHING', to='register.Sequence')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('fax_number', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete='DO_NOTHING', to='register.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_id', models.CharField(max_length=100)),
                ('report_number', models.IntegerField(max_length=100)),
                ('issue_date', models.DateField(auto_now=True)),
                ('standard', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('product', models.CharField(max_length=100, null=True)),
                ('tags', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete='DO_NOTHING', to='register.User')),
            ],
        ),
    ]
