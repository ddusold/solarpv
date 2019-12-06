from django.shortcuts import render
from .forms import RegisterForm, DashboardForm, CertificationSearchForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from .models import Certificate, User, Client
# Create your views here.


def index(request):
    return render(request, 'register/index.html')


@csrf_protect
def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = form.data['username']
        password = form.data['password']
        firstname = form.data['first_name']
        middlename = form.data['middle_name']
        lastname = form.data['last_name']
        address = form.data['address']
        phone = form.data['phone']
        email = form.data['email']
        try:
            client = Client.objects.get(pk=3)
            user = User(username=username, password=password, first_name=firstname,
                        middle_name=middlename, last_name=lastname, address=address, office_phone=phone, email=email, client=client)
            user.save()
            message = "User Added Successfully"
        except Exception as e:
            print(str(e))
            message = "Failed to add user"
    else:
        form = RegisterForm()
        message = ""

    context = {'form': form, 'message': message}
    return render(request, 'register/register.html', context)


def dashboard(request):
    form = DashboardForm()

    context = {'form': form}
    return render(request, 'register/dashboard.html', context)


@csrf_protect
def cert(request):
    if request.method == 'POST':
        form = CertificationSearchForm(request.POST)
        print(form.data['search_term'])
        try:
            match = Certificate.objects.get(
                certificate_id=form.data['search_term'])
            cert_id = getattr(match, "certificate_id")
            user = getattr(match, "user_id")
            print(user)
            report = getattr(match, "report_number")
            tags = getattr(match, "tags")
            issue_date = getattr(match, "issue_date")
            result = "<b>Certificate found: </b><br /><br />ID: " + cert_id \
                + "<br />User ID: " + str(user) \
                + "<br />Issue Date: " + str(issue_date) \
                + "<br />Tags: " + tags
            print("past result")
        except Exception:
            print(Exception)
            print("No match found, searching by tags")
            objects = Certificate.objects.all().values()
            matches = ["<b>Certificates matching keyword: </b><br/><br/>"]
            joiner = " - "
            for x in objects:
                print(x)
                if(form.data['search_term'] in x['tags']):
                    matches.append(x['certificate_id'])
            result = joiner.join(matches)

        context = {'form': form,
                   'data': '<b>Results:</b> <br /><br />' + result}
    else:
        form = CertificationSearchForm()
        context = {'form': form}

    return render(request, 'register/cert.html', context)
