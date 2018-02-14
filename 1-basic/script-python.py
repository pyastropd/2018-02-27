#!/usr/bin/env python

# Devi fare
#
#   chmod +x questo-file.py
# 
# Provalo dalla console cosi':
# python ./script-python.py '"{\"num1\":\"1.2\",\"num2\":\"1\",\"txt\":\"asd\"}"'

import sys, json

# Caricare il JSON che hai mandato dal PHP
try:
    data = json.loads(sys.argv[1])
except:
    print "ERROR: no data or bad data format provided"
    sys.exit(1)

# Per fare una prova con il php da solo
    
# Mettere tutto il JSON in un oggetto Python per poter trattare i dati come credi    
class Payload(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

# Ecco i dati in un comodo oggetto        
p = Payload(data)

# Manipolo i valori di input
p.num1 = float(p.num1)*10
p.num2 = float(p.num2)
p.txt = "ciaooo---" + p.txt + "---ciao"
p.nuovonum = ( p.num1 + p.num2 )

# Serializza in json e rispedisci il risultato al PHP
print json.dumps(p.__dict__)
