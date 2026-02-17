import xml.etree.ElementTree as ET

tree = ET.parse('XMLfromDTDexo3.xml')
root = tree.getroot()
print(root.tag)