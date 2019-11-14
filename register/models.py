from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=20)
    client_type = models.CharField(max_length=20)

    def __str__(self):
        return self.client_name


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    job_title = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    office_phone = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20)
    prefix = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete='cascade')

    def __str__(self):
        return self.first_name


class Location(models.Model):
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete='DO_NOTHING')


class Product(models.Model):
    name = models.CharField(max_length=20)
    cell_tech = models.CharField(max_length=20)
    cell_manufacturer = models.CharField(max_length=20)
    no_of_cells = models.CharField(max_length=20)
    no_of_cells_in_series = models.CharField(max_length=20)
    no_of_series_strings = models.CharField(max_length=20)
    no_of_diodes = models.CharField(max_length=20)
    length = models.CharField(max_length=20)
    width = models.CharField(max_length=20)
    superstate_type = models.CharField(max_length=20)
    superstate_manufacturer = models.CharField(max_length=20)
    substrate_type = models.CharField(max_length=20)
    substrate_manufacturer = models.CharField(max_length=20)
    frame_type = models.CharField(max_length=20)
    frame_adhesive = models.CharField(max_length=20)
    encapsulate_type = models.CharField(max_length=20)
    encapsulate_manufacturer = models.CharField(max_length=20)
    junction_box_type = models.CharField(max_length=20)
    junction_box_manufacturer = models.CharField(max_length=20)


class Standard(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    published_on = models.DateField()


class Service(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    fl_required = models.CharField(max_length=20)
    fl_frequency = models.CharField(max_length=20)
    standard = models.ForeignKey(Standard, on_delete='DO_NOTHING')


class Sequence(models.Model):
    name = models.CharField(max_length=20)


class Performance(models.Model):
    product = models.ForeignKey(Product, on_delete="DO_NOTHING")
    sequence_id = models.ForeignKey(Sequence, on_delete="DO_NOTHING")
    max_voltage = models.CharField(max_length=20)
    voc = models.CharField(max_length=20)
    isc = models.CharField(max_length=20)
    vmp = models.CharField(max_length=20)
    imp = models.CharField(max_length=20)
    pmp = models.CharField(max_length=20)
    ff = models.CharField(max_length=20)


class Certificate(models.Model):
    certificate_id = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete='DO_NOTHING')
    report_number = models.IntegerField()
    issue_date = models.DateField(auto_now='false')
    standard = models.ForeignKey(Standard, on_delete='DO_NOTHING')
    location = models.ForeignKey(Location, on_delete='DO_NOTHING')
    product = models.ForeignKey(Product, on_delete='DO_NOTHING')
