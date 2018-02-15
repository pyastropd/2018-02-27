#!/usr/bin/env python3

import sys, json
import numpy as np
#from numpy.polynomial.chebyshev import chebval,chebfit
from astropy.modeling import models, fitting

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
# # I dati di input
npts=p.npoints
noise=p.sigmanoise
stddev=p.sigmadev

# I dati fissi
amplitude=5.01
mean=4.1

# generate the data
x=np.random.uniform(-25,25,npts)

f = models.Gaussian1D(amplitude=amplitude, mean=mean, stddev=stddev)
# add noise
y=f(x)+np.random.normal(loc=0,scale=noise,size=npts)

# p0=[-.1,-1.1,-2.1,0.3,-1.1]

# # generate datapoints
# x=np.random.uniform(-2,2,npts)
# y=chebval(x,p0)
# # add some noise
# y+=np.random.randn(*y.shape)*noise
#########################################################

keys=["x","y"]

# https://stackoverflow.com/questions/29736027/creating-json-from-lists-using-zip

print(json.dumps([dict(zip(keys, row)) for row in zip(x,y)], indent=1))
