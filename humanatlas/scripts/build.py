import numpy as np, json, base64
from reg2 import warp
from fit import WZ, WZK
from cl import centerline, tosim
from dec import mesh, P
def WZi(z):
    if z>=WZK[0][1]: return z
    for i in range(1,len(WZK)):
        if z>=WZK[i][1]:
            a0,b0=WZK[i-1]; a1,b1=WZK[i]; return a0+(z-b0)*(a1-a0)/(b1-b0)
    a,b=WZK[-1]; return z-(b-a)
def Vm(n):
    v,f=mesh(n); v=tosim(v); v[:,1]-=1549; return v,f
def cl(n,k=14):
    c,L=centerline(n,k); c=c.copy(); c[:,1]-=1549; return warp(c)
def design(pts): return [[round(float(x),2),round(float(y),2),round(float(WZi(z)),2)] for x,y,z in pts]
def resample(p,k):
    p=np.asarray(p); L=np.r_[0,np.cumsum(np.linalg.norm(np.diff(p,axis=0),axis=1))]; t=np.linspace(0,L[-1],k)
    return np.c_[[np.interp(t,L,p[:,i]) for i in range(3)]].T
O={}
# Globo
sv,_=Vm('Sclera (right)'); sw=warp(sv); c=sw.mean(0); R=np.linalg.norm(sw-c,axis=1).mean()
O['GLOBE_C']=design([c])[0]; O['GLOBE_R']=round(float(R),2)
# Músculos: de vértice (posterior) a anterior
for key,n in [('MRECT','Medial rectus muscle (right)'),('IRECT','Inferior rectus muscle (right)'),('SRECT','Superior rectus muscle (right)'),('LRECT','Lateral rectus muscle (right)'),('SOBL','Superior oblique muscle (right)')]:
    p=cl(n,10)
    if p[0,2]>p[-1,2]: p=p[::-1]
    O[key]=design(p)
# Nervio óptico: globo → quiasma; se divide en la cara del esfenoides (z F2 = WZ(-67.5))
p=cl('Optic nerve (II) (right)',30)
if p[0,2]<p[-1,2]: p=p[::-1]          # de anterior a posterior
zc=WZ(-67.5); i=int(np.argmin(abs(p[:,2]-zc)))
orb=p[:i+1]; can=p[i:]
can=can[can[:,0]>3]                  # hasta antes del quiasma
O['OPTORB']=design(resample(orb,7)); O['OPTIC']=design(resample(can,4))
O['OPTORB'][-1]=O['OPTIC'][0]
# Carótida: de abajo (paraclival) hacia la supraclinoidea
p=cl('Internal carotid artery (right)',40)
if p[0,1]>p[-1,1]: p=p[::-1]
p=p[p[:,1]>4]
O['CAROTID']=design(resample(p,10))
# Basilar
p=cl('Basilar artery',6); p=p[np.argsort(p[:,1])]; p[:,0]=0
O['BASILAR']=design(resample(p,3))
# Etmoidales: tramo transversal (lateral → medial), extendido hasta la papirácea (x=18.8)
for key,n in [('AEA','Anterior ethmoidal artery (right)'),('PEA','Posterior ethmoidal artery (right)')]:
    p=cl(n,24)
    if p[0,0]<p[-1,0]: p=p[::-1]
    j=int(np.argmin(p[:,0])); q=p[:j+1]
    d=q[0]-q[min(3,len(q)-1)]; d/=np.linalg.norm(d)
    if q[0,0]<18.8: q=np.r_[[q[0]+d*(18.8-q[0,0])/max(d[0],0.2)],q]
    O[key]=design(resample(q,3))
# AEA y PEA fueron puntos de registro: no son una medición independiente, se dejan como en el Fantoma 2
O.pop('AEA',None); O.pop('PEA',None)
# Órbita: el contenido orbitario no puede quedar medial a la papirácea / pared lateral del esfenoides (x=18.5)
for key,r in [('MRECT',2.0),('IRECT',2.0),('SRECT',1.9),('LRECT',2.0),('SOBL',1.1),('OPTORB',2.1)]:
    pts=O[key]; n=len(pts)
    for i,p in enumerate(pts):
        if key=='OPTORB' and i==n-1: continue   # entrada del canal óptico
        if -95<p[2]<-10: p[0]=round(max(p[0],18.5+r+0.4),2)
gc=O['GLOBE_C']; gc[0]=round(max(gc[0],18.5+O['GLOBE_R']+2.5),2)
if __name__=='__main__':
    print(json.dumps(O))
    json.dump(O,open('overrides.json','w'))
