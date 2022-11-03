import calendar
import datetime
import json
import app.views
from django.shortcuts import render, redirect
from django.http import response, request, HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from app.forms import Auth, Register, MofonainaForm
from app.models import User, Mofonaina, Sudo, Sampana, Rafitra, Asa, Fampianarana, Vaovao, Fandaharana
from app.litorjia import Litorjia
from app.superuser import account

domain = 'http://localhos:8000/'



def session_set(request):
    try:
        session = request.session['id']
        return request.session['id']
    except KeyError:
        return False


# about
def terms(request):
    return render(request, 'terms.html', locals())


def hiala(request):
    del request.session['id']
    return redirect(home)


def home(request):
    litorjia = Litorjia
    title = 'FJKM CENHOSOA'
    url = 'mofonaina/'
    return render(request, 'base.html', locals())


def rooter(request):
    litorjia = Litorjia
    if request.method == 'GET':
        try:
            url = request.GET['url']
            if url == '':
                return redirect(home)
            title = url.split('/')[0]
            return render(request, 'base.html', locals())
        except KeyError:
            url = 'mofonaina/'
            title = 'FJKM CENHOSOA'
            return render(request, 'base.html', locals())
    else:
        url = 'mofonaina/'
        title = 'FJKM CENHOSOA'
        return render(request, 'base.html', locals())


def auth(request):
    litorjia = Litorjia
    if app.views.session_set(request) is False:
        # updating data ?
        form = Auth(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            tel = form.cleaned_data['tel']
            try:
                sudo = Sudo.objects.get(tel=int(tel))
                if check_password(password, sudo.password):
                    request.session['id'] = sudo.id

                    # one page

                    if sudo.name == 'pasteur':
                        url = 'mofonaina/'
                        title = 'MOFONAINA'
                        return render(request, 'tab/mofonaina.html', locals())
                    else:
                        title = sudo.name
                        return redirect('http://localhost:8000/sudo/{}'.format(title))

                else:
                    error_msg = 'Hamarinio ny teny miafina'
                    return render(request, 'auth.html', locals())

            except Sudo.DoesNotExist:
                error_msg = 'Azafady, hamarino ny laharana finday'
                return render(request, 'auth.html', locals())

        else:
            form = Auth()
        return render(request, 'auth.html', locals())

    else:
        # create
        try:
            type_update = request.POST['type']
            sampana_name = request.POST['sudo_name']
            match type_update:
                case 'sary':
                    sampana_picture = request.FILES.get('picture', False)
                    sampana_url = request.POST['url']

                    msg = ''
                    try:
                        sampana = Sampana.objects.get(name=sampana_name)
                        sampana.picture.delete()
                    except Sampana.DoesNotExist:
                        sampana = Sampana()

                    if sampana_picture is not False:
                        sampana.picture = sampana_picture
                        sampana.name = sampana_name
                        sampana.save()
                        sudo = Sudo.objects.get(id=app.views.session_set(request))
                        return redirect('http://localhost:8000/sudo/{}'.format(sudo.name))
                    else:
                        import requests
                        url = sampana_url
                        url_request = requests.get(url)

                        if url_request.status_code != 200:
                            msg = 'Url Non Valid'
                            return HttpResponse(msg)
                        elif 'image' not in url_request.headers['Content-Type']:
                            msg = "Pas d'Image detecté"
                            return HttpResponse(msg)
                        else:
                            sampana.picture = sampana_url
                            sampana.name = sampana_name

                            sudo = Sudo.objects.get(id=app.views.session_set(request))
                            sampana.save()
                            return redirect('http://localhost:8000/sudo/{}'.format(sudo.name))

                case 'famaritana':
                    famariparitana = request.POST['famariparitana']
                    try:
                        sampana = Sampana.objects.get(name=sampana_name)
                    except Sampana.DoesNotExist:
                        sampana = Sampana()

                    sampana.famariparitana = famariparitana
                    sampana.save()

                    sudo = Sudo.objects.get(id=app.views.session_set(request))
                    return redirect('http://localhost:8000/sudo/{}'.format(sudo.name))

                case 'rafitra':
                    name = request.POST['name']
                    function = request.POST['function']
                    picture = request.FILES.get('picture', False)
                    url = request.POST['url']
                    sudo_name = request.POST['sudo_name']

                    rafitra = Rafitra()
                    rafitra.name = name
                    rafitra.function = function
                    rafitra.sudo = sudo_name
                    rafitra.type = request.POST['type_rafitra']

                    if picture is not False:
                        rafitra.picture = picture
                    else:
                        import requests
                        url_request = requests.get(url)
                        if url_request.status_code != 200:
                            msg = 'Url Non Valid'
                            return HttpResponse(msg)
                        elif 'image' not in url_request.headers['Content-Type']:
                            msg = "Pas d'Image detecté"
                            return HttpResponse(msg)
                        else:
                            rafitra.picture = url

                    rafitra.save()

                    sudo = Sudo.objects.get(id=app.views.session_set(request))
                    return redirect('http://localhost:8000/sudo/{}'.format(sudo.name))

                case 'asa':
                    sudo_name = request.POST['sudo_name']
                    content = request.POST['content']
                    type = request.POST['type']
                    title = request.POST['title']

                    asa = Asa()
                    asa.content = content
                    asa.type = type
                    asa.sudo = sudo_name
                    asa.title = title
                    asa.save()
                    sudo = Sudo.objects.get(id=app.views.session_set(request))
                    return redirect('http://localhost:8000/sudo/{}'.format(sudo.name))

                case 'fampianarana':
                    sudo_name = request.POST['sudo_name']
                    content = request.POST['content']
                    type = request.POST['type']
                    title = request.POST['title']

                    fampianarana = Fampianarana()
                    fampianarana.content = content
                    fampianarana.type = type
                    fampianarana.sudo = sudo_name
                    fampianarana.title = title
                    fampianarana.save()
                    sudo = Sudo.objects.get(id=app.views.session_set(request))
                    return redirect('http://localhost:8000/sudo/{}'.format(sudo.name))

                case 'vaovao':
                    sudo_name = request.POST['sudo_name']
                    content = request.POST['content']
                    type = request.POST['type']
                    title = request.POST['title']
                    sokajy = request.POST['sokajy']

                    vaovao = Vaovao()
                    vaovao.content = content
                    vaovao.type = type
                    vaovao.sudo = sudo_name
                    vaovao.title = str(title).capitalize()
                    vaovao.sokajy = sokajy
                    vaovao.save()
                    sudo = Sudo.objects.get(id=app.views.session_set(request))
                    return redirect('http://localhost:8000/sudo/{}'.format(sudo.name))

                case 'mofonaina':
                    content = request.POST['content']
                    title = request.POST['title']

                    new_mofonaina = Mofonaina()
                    new_mofonaina.title = title
                    new_mofonaina.content = content

                    new_mofonaina.save()
                    return redirect(mofonaina)

        except KeyError:
            # sudo ?
            try:
                sudo = Sudo.objects.get(id=app.views.session_set(request))
                if sudo.name == 'pasteur':
                    url = 'mofonaina/'
                    title = 'MOFONAINA'
                    return render(request, 'tab/mofonaina.html', locals())
                else:
                    return redirect('http://localhost:8000/sudo/{}'.format(sudo.name))
            except KeyError:
                user = User.objects.get(tel=int(request.POST['tel']))
                return HttpResponse('Votre id est {}'.format(user.id))


def register(request):
    secondary_color = Litorjia.secondary_color
    form = Register(request.POST)

    if form.is_valid():
        password = form.cleaned_data['password']
        repeate = request.POST['repeate']
        tel = form.cleaned_data['tel']
        # verification si les deux mots de passe sont les même
        if password != repeate:
            error_msg = 'Tsy mitovy ny tent miafina roa'
            return render(request, 'register.html', locals())
        else:
            try:
                sudo = Sudo.objects.get(tel=tel)
                error_msg = 'Efa misy Mampiasa io laharana finday io'
                return render(request, 'register.html', locals())
            except Sudo.DoesNotExist:
                sudo = Sudo()
                sudo.tel = form.cleaned_data['tel']
                sudo.name = form.cleaned_data['name']
                sudo.password = make_password(password, None, 'default')
                sudo.save()
                return redirect('http://localhost:8000/sudo/{}'.format(sudo.name))
    else:
        form = Register()
        return render(request, 'register.html', locals())


def sudo(request, name):
    litorjia = Litorjia
    # session set ?
    session = app.views.session_set(request)
    if session is False:
        return redirect(auth)
    else:
        # sudo logged in ?
        try:
            sudo = Sudo.objects.get(id=session)
        except Sudo.DoesNotExist:
            error_msg = 'Azafady fa tsy Fantatra ianao'
            return render(request, 'register.html', locals())

        # loading sudo account
        with open('app/api/sudo.json') as account:
            account = json.load(account)

        # sudo ?
        try:
            if account[sudo.name]['id'] == sudo.id:
                sampana_list = ['safif', 'dorkasy', 'sampati', 'sa', 'slk', 'svm', 'stk', 'vfl']
                superuser = True
                if sudo.name in sampana_list:
                    superuser_sampana = True
                    url = 'sampana/'
                    title = 'SAMPANA'
                    return redirect(sampana)
                else:
                    return redirect(home)
        except KeyError:
            return HttpResponse('Votre id est {}'.format(sudo.id))


def goto(request):
    primary_color = Litorjia.primary_color
    secondary_color = Litorjia.secondary_color
    litorjia = Litorjia
    try:
        template = request.GET['template']
        id = request.GET['id']
        if id == 'undefined':
            raise ValueError

        tabulation = request.GET['tab']
        match tabulation:
            case 'sampana':
                try:
                    sampana_user = False
                    if session_set(request) is not False:
                        try:
                            sudo = Sudo.objects.get(id=session_set(request))

                            sampana_list = ['safif', 'dorkasy', 'sampati', 'sa', 'slk', 'svm', 'stk', 'vfl']
                            if sudo.name in sampana_list:
                                sampana = Sampana.objects.get(name=sudo.name)
                                sampana_user = True
                        except:
                            pass
                    sampana = Sampana.objects.get(id=id)
                    name = sampana.name
                    couverture = sampana.picture

                    # url ?
                    str_couverture = str(couverture).split('/')
                    if str_couverture[0] not in ['http:', 'https:']:
                        couverture = '/app/{}'.format(couverture)

                    famariparitana = sampana.famariparitana

                    # rafitra
                    rafitra = Rafitra.objects.filter(sudo=name)
                    if len(rafitra) == 0:
                        rafitra = 'Mbola tsy misy'
                        return render(request, 'check/{}/{}.html'.format(tabulation, template), locals())
                    # asa
                    asa = Asa.objects.filter(sudo=name).order_by('id').reverse()
                    data = []
                    for k in range(len(asa)):
                        i = k % 2
                        if i == 0:
                            data.append({
                                'float': 'left',
                                'asa': asa[k]
                            }
                            )
                        else:
                            data.append({
                                'float': 'right',
                                'asa': asa[k]
                            }
                            )

                    # fampianarana
                    fampianarana = Fampianarana.objects.filter(sudo=name).order_by('id').reverse()


                except KeyError:
                    with open('app/api/sampana.json') as sampana:
                        sampana = json.load(sampana)[name]

                    name = sampana['name']
                    rafitra = sampana['organigramme']
                    couverture = sampana['couverture']
                    famariparitana = sampana['famariparitana']

                return render(request, 'check/{}/{}.html'.format(tabulation, template), locals())
            case 'vaovao':
                query = request.GET['id']
                order = request.GET['template']

                match order:
                    case 'null':
                        vaovao = Vaovao.objects.all().order_by('id').reverse()
                        return render(request, 'check/vaovao.html', locals())
                    case 'search_date':
                        msg = query
                        query = query.split('-')

                        # date null ?
                        if '' in query:
                            msg = 'Daty Tsy Mety'

                        year = query[0]
                        month = query[1]
                        day = query[2]
                        date = '{}-{}-{}'.format(year, month, day)

                        # filter
                        try:
                            vaovao = Vaovao.objects.filter(date=date)
                        except :
                            date = '{}/{}/{}'.format(year, month, day)
                            msg = 'Hamarino Tsara Azafady ny Daty : {} '.format(date)
                            return HttpResponse("<h3 style='text-align:center'> {} </h3>".format(msg))
                        if len(vaovao) == 0:
                            date = '{}/{}/{}'.format(year, month, day)
                            msg = 'Tsy Misy Ny Fangatahana Daty : {} '.format(date)
                            return HttpResponse("<h3 style='text-align:center'> {} </h3>".format(msg))
                        else:
                            return render(request, 'check/vaovao.html', locals())

                    case 'order_sokajy':
                        sokajy = query
                        vaovao = Vaovao.objects.filter(sokajy=str(sokajy).capitalize())

                        if len(vaovao) == 0:
                            msg = 'Tsy Misy Ny Fangatahana Daty : {} '.format(sokajy)
                            return HttpResponse("<h3 style='text-align:center'> {} </h3>".format(msg))
                        else:
                            return render(request, 'check/vaovao.html', locals())

            case 'fiangonana':
                # pasteur ?
                pasteur = False
                if session_set(request) is False:
                    user = None
                else:
                    try:
                        session = session_set(request)
                        sudo = Sudo.objects.get(id=session)
                        if sudo.name == 'pasteur':
                            pasteur = True
                    except User.DoesNotExist:
                        pass

                option = request.GET['template']
                match option:
                    case 'fandaharana':  # fandaharana
                        fandaharana = Fandaharana.objects.all().reverse()

                return render(request, 'check/fiangonana/{}.html'.format(option), locals())

            case 'about':
                option = request.GET['template']
                match option:
                    case 'hiala':
                        try:
                            del request.session['id']
                            msg = 'Tafiala soamatsar ianao !'
                            return HttpResponse("<h3 style='text-align:center'> {} </h3>".format(msg))
                        except:
                            msg = 'Efa tafiala ianao'
                            return HttpResponse("<h3 style='text-align:center'> {} </h3>".format(msg))

                    case 'superuser':
                        return redirect(auth)
                return HttpResponse(option)

            case 'stream':
                import app.streamer
                my_stream = app.streamer.stream()
                return my_stream

    except KeyError:
        return HttpResponse('Une erreur s\'est reproduite')
    except ValueError:
        return HttpResponse('<h3 style="text-align:center">Tsy Misy</h3>')


def sudoQuery(request):
    litorjia = Litorjia
    primary_color = Litorjia.primary_color
    secondary_color = Litorjia.secondary_color

    try:
        query = request.GET['q']
        id = request.GET.get('id', False)

        sudo = request.GET['sudo']
        sudo_account = Sudo.objects.get(id=id)
        name = sudo_account.name
        primary_color = Litorjia.primary_color
        secondary_color = Litorjia.secondary_color

        match sudo:
            case 'sampana':
                try:
                    sampana_user = True
                    sampana = Sampana.objects.get(name=str(name).lower())
                    couverture = sampana.picture

                    # url ?
                    str_couverture = str(couverture).split('/')
                    if str_couverture[0] not in ['http:', 'https:']:
                        couverture = '/app/{}'.format(couverture)

                    famariparitana = sampana.famariparitana

                    # rafitra
                    rafitra = Rafitra.objects.filter(sudo=name)
                    if len(rafitra) == 0:
                        rafitra = 'Mbola tsy misy'

                    # asa
                    asa = Asa.objects.filter(sudo=name).order_by('id').reverse()
                    data = []
                    for k in range(len(asa)):
                        i = k % 2
                        if i == 0:
                            data.append({
                                'float': 'left',
                                'asa': asa[k]
                            }
                            )
                        else:
                            data.append({
                                'float': 'right',
                                'asa': asa[k]
                            }
                            )

                    # fampianarana
                    fampianarana = Fampianarana.objects.filter(sudo=name).order_by('id').reverse()


                except KeyError:
                    with open('app/api/sampana.json') as sampana:
                        sampana = json.load(sampana)[sudo_account.name]

                    name = sampana['name']
                    rafitra = sampana['organigramme']
                    couverture = sampana['couverture']
                    famariparitana = sampana['famariparitana']

                return render(request, 'sudo/{}/{}.html'.format(sudo, query), locals())

            case 'vaovao':
                sudo_account = True
                vaovao = Vaovao.objects.all().order_by('id').reverse()
                return render(request, 'check/vaovao.html', locals())
    except KeyError:
        return HttpResponse('none')

    except ValueError:
        return HttpResponse('Value Error')


# tabs
def mofonaina(request):
    litorjia = Litorjia
    # session set or connected?
    pasteur = False
    if app.views.session_set(request) is False:
        user = None
    else:
        try:
            session = app.views.session_set(request)
            # user
            sudo = Sudo.objects.get(id=session)
            if sudo.name == 'pasteur':
                pasteur = True
        except User.DoesNotExist:
            pass

    primary_color = Litorjia.primary_color
    secondary_color = Litorjia.secondary_color

    # article
    mofonainas = Mofonaina.objects.all().order_by('id').reverse()

    url = 'mofonaina/'
    title = 'MOFONAINA'  # vardumps ?

    return render(request, 'tab/mofonaina.html', locals())


def sampana(request):
    # session sest or connected ?
    if app.views.session_set(request) is False:
        user = None
    else:
        try:
            session = app.views.session_set(request)
            # sudo ?
            sudo = Sudo.objects.get(id=session)
            # sampana ?
            sampana_list = ['safif', 'dorkasy', 'sampati', 'sa', 'slk', 'svm', 'stk', 'vfl']
            if sudo.name in sampana_list:
                sampana = Sampana.objects.get(name=sudo.name)
                sampana_user = True
                url = 'sampana/'
                title = 'SAMPANA'
                return render(request, 'tab/sampana.html', locals())
        except Sampana.DoesNotExist:
            return HttpResponse('not in sampana')

    url = 'sampana/'
    title = 'SAMPANA'
    return render(request, 'tab/sampana.html', locals())


def vaovao(request):
    # session set ?
    if app.views.session_set(request) is False:
        user = None
    else:
        try:
            session = app.views.session_set(request)
            # user
            sudo = Sudo.objects.get(id=session)
            if sudo.name == 'vaovao':
                sudo_account = True
        except User.DoesNotExist:
            pass
    return render(request, 'tab/vaovao.html', locals())


def fiangonana(request):
    # session set or connected?
    pasteur = False
    if app.views.session_set(request) is False:
        user = None
    else:
        try:
            session = app.views.session_set(request)
            # user
            sudo = Sudo.objects.get(id=session)
            if sudo.name == 'pasteur':
                pasteur = True
        except User.DoesNotExist:
            pass

    return render(request, 'tab/fiangonana.html', locals())

def hafa(request):

    return render(request, 'tab/hafa.html', locals())


def hikaroka(request):
    return render(request, 'tab/fikarohana.html', locals())


def mofonaina_vaovao(request):
    if app.views.session_set(request) is False:
        return redirect(auth)
    else:
        session = app.views.session_set(request)
        primary_color = Litorjia.primary_color
        secondary_color = Litorjia.secondary_color
        # user
        user = User.objects.get(id=session)

        #  pasteur ?
        if user.id == account['pasteur']['id']:
            form = MofonainaForm(request.POST, request.FILES)
            if form.is_valid():
                mofonaina = Mofonaina()
                mofonaina.title = form.cleaned_data['title']
                mofonaina.content = form.cleaned_data['content']
                mofonaina.author_id = session
                mofonaina.author_name = user.full_name
                mofonaina.save()
                return redirect(mofonaina)
            else:
                form = MofonainaForm()
                return render(request, 'creation/mofonaina.html', locals())
        else:
            return HttpResponse("Tsy mahazo alalaina ato amin`ity rohy ity ianao")


def mofonaina_mamaky(request, id):
    primary_color = Litorjia.primary_color
    secondary_color = Litorjia.secondary_color
    # is exits
    try:
        mofonaina = Mofonaina.objects.get(id=id)
        return render(request, 'check/mofonaina.html', locals())

    except Mofonaina.DoesNotExist:
        error_msg = 'Tsy misy ny Mofonaina nangatahinao'
        return HttpResponse(error_msg)


def view_sampana(request, sampana):
    name = str(sampana).lower()
    try:
        # data
        sampana = Sampana.objects.get(name=name)

        # photo
        couverture = sampana.picture
        str_couverture = str(couverture).split('/')
        if str_couverture[0] not in ['http:', 'https:']:
            couverture = '/app/{}'.format(couverture)

        # famariparitana
        famariparitana = sampana.famariparitana

        # rafitra
        rafitra = Rafitra.objects.filter(sudo=name)
        if len(rafitra) == 0:
            rafitra = 'Mbola tsy misy'

        # asa
        asa = Asa.objects.filter(sudo=name).order_by('id').reverse()
        data = []
        for k in range(len(asa)):
            i = k % 2
            if i == 0:
                data.append({
                    'float': 'left',
                    'asa': asa[k]
                }
                )
            else:
                data.append({
                    'float': 'right',
                    'asa': asa[k]
                }
                )

        # fampianarana
        fampianarana = Fampianarana.objects.filter(sudo=name).order_by('id').reverse()
    except Sampana.DoesNotExist:
        with open('app/api/sampana.json') as sampana:
            sampana = json.load(sampana)[name]

        name = sampana['name']
        rafitra = sampana['organigramme']
        couverture = sampana['couverture']
        famariparitana = sampana['famariparitana']

    return render(request, 'check/sampana.html', locals())


def boite_a_idee(request):
    content = request.POST['content']
    mailaka = request.POST['mailaka']

    # mailto
    print(content)
    return HttpResponse('Lasa aoa amatsara ny hevitrao, misaotra !')


def update(request):
    view = request.GET['view']
    arg = request.GET['arg']
    data = request.GET['data']

    match view:
        case 'mofonaina':
            data = data.split('///')
            print(data)
            id = data[0]
            title = data[1]
            content = data[2]
            try:
                data_mofonaina = Mofonaina.objects.get(id=int(id))
                data_mofonaina.title = title
                data_mofonaina.content = content
                data_mofonaina.save()
                msg = 'Tontosa ny fangatahao'
            except:
                msg = 'Misy olana'
            return HttpResponse("<h3 style='text-align:center'> {} </h3>".format(msg))



def remove(request):
    view = request.GET['view']
    arg = request.GET['arg']
    data = request.GET['data']
    models = {
        'user': User, 'mofonaina': Mofonaina,
        'sudo': Sudo, 'sampana': Sampana,
        'rafitra': Rafitra, 'asa': Asa,
        'fampianarana': Fampianarana, 'vavao': Vaovao, 'fandaharana': Fandaharana
    }
    try:
        view = models[str(view).lower()]
        view = view.objects.get(id=int(data))
        view.delete()
        msg = 'Tontosa soa amatsara ny fangatahianao'
    except:
        msg = 'Tsy tontosa ny fangatahanao'
    return HttpResponse("<h3 style='text-align:center'> {} </h3>".format(msg))


def downloader(request):
    #  to download element
    from app.downloader import download
    from django.http import FileResponse
    db = request.GET['db']
    id = request.GET['id']
    file_name = ''
    models = {
        'user': User, 'mofonaina': Mofonaina,
        'sudo': Sudo, 'sampana': Sampana,
        'rafitra': Rafitra, 'asa': Asa,
        'fampianarana': Fampianarana, 'vavao': Vaovao, 'fandaharana': Fandaharana
    }
    try:
        model = models[str(db).lower()]
        data = model.objects.get(id=int(id))
        file = download(model, db, int(id))
        # downloading pdf file
        return FileResponse(open(file, 'rb'), as_attachment=True)
    except KeyError:
        return HttpResponse('Erreur')
