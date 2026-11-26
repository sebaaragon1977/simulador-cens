import numpy as np
from fit import WZ
def F(x,y,z): return [x,y,WZ(z)]
# Región A: órbita y techo etmoidal
LA=[([11.6,49.4,54.1],F(18.8,44.6,-31.5)),   # AEA en la papirácea
    ([12.0,46.6,44.2],F(18.8,42.0,-56.5)),   # PEA en la papirácea
    ([11.9,25.7,68.7],F(18.6,28,-14.5)),     # nasolagrimal sup
    ([2.4,45.8,55.0],F(5,45.1,-28.5))]       # AEA medial
for z,zs in ((44,-56),(52,-45),(60,-35)):
    LA+= [([12.5,45.0,z],F(18.5,43,zs)),([15.0,33.0,z],F(18.5,33,zs))]
# Región B: esfenoides, silla y clivus
LB=[([14.1,34.3,39.7],F(18.5,19,-66.3)),([14.1,56.0,39.7],F(18.5,42,-66.3)),([14.1,34.3,22.1],F(18.5,19,-90)),([14.1,56.0,22.1],F(18.5,42,-90)),
    ([0,52.1,18.2],F(0,31,-93)),([0,41.0,4.0],F(0,20,-96)),([12.0,46.6,44.2],F(18.8,42.0,-56.5))]
def g(x): return np.minimum(1,np.abs(x)/10)   # el corrimiento lateral se anula en la línea media
def sim(L, lat=True):
    A=np.array([a for a,_ in L]); B=np.array([b for _,b in L])
    # escala isótropa s, corrimiento lateral tx (simétrico), traslación ty,tz
    M=[];r=[]
    for a,b in zip(A,B):
        M.append([a[0],g(a[0])*np.sign(a[0]) if lat else 0,0,0]); r.append(b[0]); M.append([a[1],0,1,0]); r.append(b[1]); M.append([a[2],0,0,1]); r.append(b[2])
    (s,tx,ty,tz),*_=np.linalg.lstsq(np.array(M),np.array(r),rcond=None)
    def T(p):
        p=np.atleast_2d(p).astype(float); q=p*s+[0,ty,tz]; q[:,0]+=tx*g(p[:,0])*np.sign(p[:,0]); return q
    T.tx=tx
    res=np.linalg.norm(T(A)-B,axis=1)
    return T,s,(ty,tz),res
TA,sA,tA,rA=sim(LA); TB,sB,tB,rB=sim(LB)
tA=(TA.tx,)+tuple(tA); tB=(TB.tx,)+tuple(tB)
def warp(p):
    p=np.atleast_2d(p); a=TA(p); b=TB(p)
    zf=b[:,2]; w=np.clip((zf-WZ(-66))/(WZ(-50)-WZ(-66)),0,1)[:,None]   # 1 = órbita/etmoides, 0 = esfenoides
    return w*a+(1-w)*b
if __name__=='__main__':
    print('A s=%.3f t=%s res=%s'%(sA,np.round(tA,1),np.round(rA,1)))
    print('B s=%.3f t=%s res=%s'%(sB,np.round(tB,1),np.round(rB,1)))
