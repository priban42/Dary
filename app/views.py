from django.shortcuts import render

# Create your views here.
from app.models import Dar

def delete_everything():
    Dar.objects.all().delete()


def resetDB(request):
    example()

def example():
    delete_everything()
    Dar(name = "Žehlička", text="Ideálně napařovací.", rezervace=False, img_url="http://mmgg.mysteria.cz/dary/zehlicka.jpg").save()
    Dar(name = "Žehlící prkno",
    text="",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/zehlici_prkno.jpg").save()
    Dar(name = "Vysavač",
    text="Aby byl skladný.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/vysavac.jpg").save()
    Dar(name = "Sada na uklízení",
    text="S obdelníkovým zacvakávacím hadříkem (aby se nemusel nandavat pokaždé znovu) a odstředivkou. Příklad třeba <a href=\"https://www.leifheit-shop.cz/uklidova-sada-twist-system-new-m-leifheit-52014?gclid=CjwKCAjw_LL2BRAkEiwAv2Y3Sd3oeorq_iVjagbD_eU2-qrtOvaY6yKkK4EskRJ88TwvcKEh67Yb7xoC7vYQAvD_BwE\">tento</a> nebo <a href=\"https://www.mall.cz/sety-mopy/vileda-ultramax-set-box?gclid=CjwKCAjw_LL2BRAkEiwAv2Y3SZC_cD6O_uUmAfR2u1AFqlw-1okumvVYt0w-2Dx4jrsTNNzYz0rv7RoCao0QAvD_BwE\">tento</a>.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/mop.jpg").save()
    Dar(name = "Kuchyňská odměrka",
    text="Může být laboratorní odměrný válec - pokud možno spíše nižší než vyšší, objem 250 ml či 300 ml.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/odmerka.jpg").save()
    Dar(name = "Domácí lékárnička",
    text="Nějakou pěknou, praktickou, vybavenou takovým běžným vybavením lékárničky do domácnosti (obinadla, náplasti, černé uhlí, analgetika, desinfekce atd.) Obrázek výše je spíše ilustrativní. Ikdyž...",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/lekarnicka.jpg").save()
    Dar(name = "Kráječ na vajíčka",
    text="Ten obrázek vypadá spíše jako postel, ale věřte mi, není to postel. Je to kráječ na vajíčka.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/krajec_na_vajicka.jpg").save()
    Dar(name = "Stínomilná kokedama",
    text="",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/kokedama.jpg").save()
    Dar(name = "Silikonový vál na těsto",
    text="",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/silikonovy_val.jpg").save()
    Dar(name = "Velká pokojovka",
    text="Například fíkus, chamedorea, shefflera...Tak, aby nám to zvládlo severní okna.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/pokojovka.jpg").save()
    Dar(name = "Řasokoule v kulatém akvárku",
    text=":-)",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/rasokoule.jpg").save()
    Dar(name = "Septuaginta",
    text="Řecký překlad Starého zákona.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/septuaginta.jpg").save()
    Dar(name = "Žehlička",
    text="Ideálně napařovací.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/zehlicka.jpg").save()
    Dar(name = "Desková hra: Osadníci z Katanu",
    text="",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/osadnici_z_katanu.jpg").save()
    Dar(name = "Desková hra: Carcassonne",
    text="Nejlépe Mindok Carcassonne Big Box 2017, neboť je to rozšířená verze.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/carcassonne.jpg").save()
    Dar(name = "Desková hra: Dostihy a sázky",
    text="Ideálně pokud by se dalo sehnat staré vydání...",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/dostihy_a_sazky.jpg").save()
    Dar(name = "Společenská hra: Jungle Speed",
    text="",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/junglespeed.jpg").save()
    Dar(name = "Společenská hra: Citadela",
    text="",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/citadela.jpg").save()
    Dar(name = "Společenská hra: BANG!",
    text="Základní balíček plus rozšíření \"Fistful\", \"Město duchů\" a \"Divoký západ\".",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/bang.jpg").save()
    Dar(name = "Dortová forma",
    text="Nějaká taková střední velikost.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/dortova_forma.jpg").save()
    Dar(name = "Sada zapékacích mističek",
    text="Ideálně napařovací.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/zepekaci_misky.jpg").save()
    Dar(name = "Elektrický ruční šlehač",
    text="Ruční šlehač, ideálně se stojanem. Například <a href=\"https://www.mall.cz/mixery/sencor-shm-5330-eue3?gclid=CjwKCAjw_LL2BRAkEiwAv2Y3SWF3s1adC7xmRPkx3KDFEBwv2LPgvZjybUpbMaD7Lpl1d40ReIDXdBoCTz4QAvD_BwE\">tento</a>.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/rucni_slehac.jpg").save()
    Dar(name = "Dárková karta IKAE",
    text="S libovolně velkou částkou.",
    rezervace=False,
    img_url="http://mmgg.mysteria.cz/dary/ikea.jpg").save()



def seznam(request):
    #example()
    dary = Dar.objects.all()
    if (len(request.GET)) > 0 and len(request.GET['index']) > 0:
        index = int(request.GET['index'])
        Dar.objects.filter(id=index).update(rezervace=True)
    return render(request, "template_seznam.html", {'dary': dary})