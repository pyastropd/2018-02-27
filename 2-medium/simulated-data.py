#!/usr/bin/env python3

import numpy as np
import json
from astropy.modeling import models, fitting
import sys, json

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

# I dati di input
npts=p.npoints
data_sigma=p.sigmanoise
stddev=p.sigmadev

# I dati fissi
amplitude=5.01
mean=4.1

# generate the data
x=np.random.uniform(-25,25,npts)
f = models.Gaussian1D(amplitude=amplitude, mean=mean, stddev=stddev)
# add noise
y=f(x)+np.random.normal(loc=0,scale=data_sigma,size=npts)

keys=["x","y"]

# https://stackoverflow.com/questions/29736027/creating-json-from-lists-using-zip

print(json.dumps([dict(zip(keys, row)) for row in zip(x,y)], indent=1))
