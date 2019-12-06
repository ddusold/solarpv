from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_type = models.CharField(max_length=100)

    def __str__(self):
        return self.client_name


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    office_phone = models.CharField(max_length=100)
    cell_phone = models.CharField(max_length=100, null=True)
    prefix = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete='cascade')

    def __str__(self):
        return self.first_name


class Location(models.Model):
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    fax_number = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete='DO_NOTHING')


class Product(models.Model):
    name = models.CharField(max_length=100)
    cell_tech = models.CharField(max_length=100)
    cell_manufacturer = models.CharField(max_length=100)
    no_of_cells = models.CharField(max_length=100)
    no_of_cells_in_series = models.CharField(max_length=100)
    no_of_series_strings = models.CharField(max_length=100)
    no_of_diodes = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    superstate_type = models.CharField(max_length=100)
    superstate_manufacturer = models.CharField(max_length=100)
    substrate_type = models.CharField(max_length=100)
    substrate_manufacturer = models.CharField(max_length=100)
    frame_type = models.CharField(max_length=100)
    frame_adhesive = models.CharField(max_length=100)
    encapsulate_type = models.CharField(max_length=100)
    encapsulate_manufacturer = models.CharField(max_length=100)
    junction_box_type = models.CharField(max_length=100)
    junction_box_manufacturer = models.CharField(max_length=100)


class Standard(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    published_on = models.DateField()


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    fl_required = models.CharField(max_length=100)
    fl_frequency = models.CharField(max_length=100)
    standard = models.ForeignKey(Standard, on_delete='DO_NOTHING')


class Sequence(models.Model):
    name = models.CharField(max_length=100)


class Performance(models.Model):
    product = models.ForeignKey(Product, on_delete="DO_NOTHING")
    sequence_id = models.ForeignKey(Sequence, on_delete="DO_NOTHING")
    max_voltage = models.CharField(max_length=100)
    voc = models.CharField(max_length=100)
    isc = models.CharField(max_length=100)
    vmp = models.CharField(max_length=100)
    imp = models.CharField(max_length=100)
    pmp = models.CharField(max_length=100)
    ff = models.CharField(max_length=100)


class Certificate(models.Model):
    certificate_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete='DO_NOTHING')
    report_number = models.IntegerField(max_length=100)
    issue_date = models.DateField(auto_now='false')
    standard = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    product = models.CharField(max_length=100, null=True)
    tags = models.CharField(max_length=100, null=True)
    # standard = models.ForeignKey(Standard, on_delete='DO_NOTHING')
    # location = models.ForeignKey(Location, on_delete='DO_NOTHING')
    # product = models.ForeignKey(Product, on_delete='DO_NOTHING')
