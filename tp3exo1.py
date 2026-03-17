from xml.dom.minidom import parse

def getId():
    dom = parse("carnet.xml") #xml reader
    print(dom.hasChildNodes())
    for n in dom.getElementsByTagName("address"):
        if (n.hasAttribute("name")):
            print(n.getAttribute("id"))
getId()

def getNum():
    dom = parse("carnet.xml")
    print(dom.hasChildNodes())
    for n in dom.getElementsByTagName("phone"):
        print(n.childNodes.item(0).nodeValue)
getNum()
                           