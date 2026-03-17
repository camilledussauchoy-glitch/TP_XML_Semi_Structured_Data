from xml.dom.minidom import parse

#1 : Liste des titres de films
def getTitresfilms():
    dom = parse("films.xml")
    print(dom.hasChildNodes())
    l = []
    for n in dom.getElementsByTagName("TITRE"):
        l.append(n.childNodes.item(0).nodeValue)
    print(l)
    return l

#getTitresfilms()

#2 : Les titres des films parus en 1990
def getFilms1990():
    dom = parse("films.xml")
    print(dom.hasChildNodes())
    l = []
    for n in dom.getElementsByTagName("FILM"): #n est un seul film
         if (n.getAttribute("Annee") == '1990'):
            l.append(n.childNodes.item(1).childNodes.item(0).nodeValue)
    print(l)
    return l

#getFilms1990()


def getResumeAlien():
    dom = parse("films.xml")
    print(dom.hasChildNodes())
    films = dom.getElementsByTagName("FILM")
    for n in films:
        f = n.childNodes.item(1).childNodes.item(0).nodeValue
        if f == "Alien" :
            x = n.getElementsByTagName("RESUME")
            if x.length > 0:
                print(x.item(0).childNodes.item(0).nodeValue)

    return

#getResumeAlien()
    

def getBruceWillis():
    dom = parse("films.xml")
    print(dom.hasChildNodes())
    films = dom.getElementsByTagName("FILM")
    l = []
    for roles in films.getElementsByTagName("ROLES"):
        prenom = roles.childNodes.item(0)
        nom = roles.childNodes.item(1).nodeValue
        print(prenom, nom)    
        if prenom == 'Bruce' and nom == "Willis":
            l.append(n.childNodes.item(1).childNodes.item(0).nodeValue)
    print(l)
    return 

getBruceWillis()