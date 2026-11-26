from dec import *
import numpy as np, scipy.sparse as sp, scipy.sparse.csgraph as cg
def tosim(v): return np.c_[-v[:,0], v[:,1], v[:,2]]  # x lateral derecho positivo
def centerline(name, n=10, start=None):
    v,f=mesh(name); v=tosim(v)
    e=np.r_[f[:,[0,1]],f[:,[1,2]],f[:,[2,0]]]
    _n,_lab=cg.connected_components(sp.coo_matrix((np.ones(len(e)),(e[:,0],e[:,1])),shape=(len(v),)*2),directed=False)
    keep=_lab==np.argmax(np.bincount(_lab)); idx=-np.ones(len(v),int); idx[keep]=np.arange(keep.sum())
    e=e[keep[e[:,0]]&keep[e[:,1]]]; e=idx[e]; v=v[keep]
    w=np.linalg.norm(v[e[:,0]]-v[e[:,1]],axis=1)
    G=sp.coo_matrix((w,(e[:,0],e[:,1])),shape=(len(v),)*2).tocsr(); G=G.maximum(G.T)
    # extremos: punto más lejano de un punto arbitrario, y su más lejano
    d0=cg.dijkstra(G,indices=0); d0[np.isinf(d0)]=-1; a=int(np.argmax(d0))
    da,pred=cg.dijkstra(G,indices=a,return_predecessors=True); da2=da.copy(); da2[np.isinf(da2)]=-1; b=int(np.argmax(da2))
    path=[b]
    while path[-1]!=a: path.append(pred[path[-1]])
    pts=v[path]; L=np.r_[0,np.cumsum(np.linalg.norm(np.diff(pts,axis=0),axis=1))]
    t=np.linspace(0,L[-1],n); P=np.array([pts[np.argmin(abs(L-ti))] for ti in t])
    # centrar: promedio de vértices cercanos (radio adaptativo)
    out=[]
    for p in P:
        dd=np.linalg.norm(v-p,axis=1); r=max(2.0, np.percentile(dd,3)); out.append(v[dd<r].mean(0))
    out=np.array(out)
    if start is not None and np.linalg.norm(out[0]-start)>np.linalg.norm(out[-1]-start): out=out[::-1]
    return out, L[-1]
if __name__=='__main__':
    for nm in ['Anterior ethmoidal artery (right)','Posterior ethmoidal artery (right)','Optic nerve (II) (right)','Internal carotid artery (right)','Nasolacrimal duct (right)','Medial rectus muscle (right)','Maxillary artery (right)','Basilar artery']:
        c,L=centerline(nm,8)
        print(nm, round(L,1)); print(np.round(c,1).tolist())
