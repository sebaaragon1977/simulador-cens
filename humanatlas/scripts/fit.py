import numpy as np
WZK=[[-28,-28],[-40.8,-39.4],[-43,-40.5],[-50,-45.5],[-66,-51.5]]
def WZ(z):
    if z>=WZK[0][0]: return z
    for i in range(1,len(WZK)):
        if z>=WZK[i][0]:
            a0,b0=WZK[i-1]; a1,b1=WZK[i]; return b0+(z-a0)*(b1-b0)/(a1-a0)
    a,b=WZK[-1]; return z+(b-a)
# (nombre, ZA sim-frame xyz, diseño xyz)  ZA y relativo a 1549
L=[('NLD sup',[11.9,1574.7-1549,68.7],[18.6,28,-14.5]),
   ('Hasner',[8.4,1558.3-1549,58.7],[17.6,3.5,-16]),
   ('AEA x12',[11.6,1598.4-1549,54.1],[12,44.85,-30]),
   ('PEA x12',[12.0,1595.6-1549,44.2],[12,42.2,-55.5]),
   ('cara esfenoides',[None,None,39.7],[None,None,-66]),
   ('ICA rodilla ant',[13.3,1590.1-1549,24.9],[17.6,38.2,-71.5]),
   ('hipófisis',[0,1601.1-1549,18.2],[0,31,-93]),
   ('basilar',[0,1590-1549,4],[0,20,-96]),
   ('cabeza CI',[None,None,75],[None,None,-6]),
]
if __name__=='__main__':
    for nm,a,d in L:
        print(f"{nm:16s} ZA z {a[2]:6.1f}  diseño {d[2]:6.1f}  F2 {WZ(d[2]):6.1f}")
    Z=np.array([a[2] for _,a,_ in L]); F=np.array([WZ(d[2]) for *_,d in L]); G=np.array([d[2] for *_,d in L])
    for nm,T in [('F2',F),('generico',G)]:
        A=np.c_[Z,np.ones_like(Z)]; (s,b),*_=np.linalg.lstsq(A,T,rcond=None); r=T-(s*Z+b)
        print(nm,'z = %.3f*Z + %.1f'%(s,b),'resid',np.round(r,1))
        A=np.c_[np.ones_like(Z)]; b1=np.mean(T-Z); print('  escala 1: b=%.1f resid'%b1,np.round(T-Z-b1,1))
