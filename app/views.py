from django.shortcuts import render

# Create your views here.
from app.models import Dar

def delete_everything():
    Dar.objects.all().delete()

def example():
    delete_everything()
    Dar(name = "Žehlička", text="Ideálně napařovací.", rezervace=False, img_url="http://mmgg.mysteria.cz/dary/zehlicka.jpg").save()
    Dar(name="Žehlící prkno", text="Decentní.", rezervace=False, img_url="http://mmgg.mysteria.cz/dary/zehlici_prkno.jpg").save()
    Dar(name="Vysavač", text="Skladný a výkonný.", rezervace=False, img_url="http://mmgg.mysteria.cz/dary/vysavac.jpg").save()
    Dar(name="Mop", text="Se zacvakávacím hadříkem (aby se nemusel nandavat pokaždé znovu) a odstředivkou. Příklad třeba <a href=\"https://www.leifheit-shop.cz/uklidova-sada-twist-system-new-m-leifheit-52014?gclid=CjwKCAjw_LL2BRAkEiwAv2Y3Sd3oeorq_iVjagbD_eU2-qrtOvaY6yKkK4EskRJ88TwvcKEh67Yb7xoC7vYQAvD_BwE\">tento</a> nebo podobné.", rezervace=False, img_url="http://mmgg.mysteria.cz/dary/mop.jpg").save()
    Dar(name="Bagr", text="Velký a hlučný", rezervace=False,img_url="https://www.rcskladem.cz/_obchody/www.rcskladem.cz/prilohy/23/double-e-kovovy-bagr-se-17-kanalovou-vysilackou-0.jpg").save()

def seznam(request):
    #example()
    dary = Dar.objects.all()
    if (len(request.GET)) > 0 and len(request.GET['index']) > 0:
        index = int(request.GET['index'])
        Dar.objects.filter(id=index).update(rezervace=True)
    return render(request, "template_seznam.html", {'dary': dary})