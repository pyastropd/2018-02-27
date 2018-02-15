#!/usr/bin/env python3

import sys, json
import numpy as np
from numpy.polynomial.chebyshev import chebval,chebfit

# Caricare il JSON che hai mandato dal PHP
try:
    data = json.loads(sys.argv[1])
except:
    print ("ERROR: no data or bad data format provided")
    sys.exit(1)

# Mettere tutto il JSON in un oggetto Python per poter trattare i dati come credi
class Payload(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

# Ecco i dati in un comodo oggetto
p = Payload(data)

#########################################################
#x,y=zip(*[d.values() for d in p.sim]) # A volte inverte x e y (async)

x=[d['x'] for d in p.sim]
y=[d['y'] for d in p.sim]

xarr=np.array(x)
yarr=np.array(y)

# fit data with a polynomial of degree p.polydeg
pfit1=chebfit(xarr,yarr,p.polideg)

# generate best-fit lines
xfit=np.linspace(xarr.min(),xarr.max(),50)
yfit=chebval(xfit,pfit1)
#########################################################

keys=["x","y"]

# https://stackoverflow.com/questions/29736027/creating-json-from-lists-using-zip

print(json.dumps([dict(zip(keys, row)) for row in zip(xfit,yfit)], indent=1))
