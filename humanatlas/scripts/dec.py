import json,numpy as np
import os
ZA_DIR=os.environ.get('ZA_DIR','human-atlas/public/models')
D=json.load(open(ZA_DIR+'/atlas-z-anatomy.json'))
P={p['name']:p for p in D['parts']}
_cache={}
def chunk(i):
    if i not in _cache: _cache[i]=open(ZA_DIR+'/atlas-z-anatomy-%d.bin'%i,'rb').read()
    return _cache[i]
def mesh(name):
    p=P[name]; b=chunk(p['chunk'])
    v=np.frombuffer(b,np.float32,p['vertexCount']*3,p['positions']).reshape(-1,3).astype(float)*1000
    f=np.frombuffer(b,np.uint32,p['indexCount'],p['indices']).reshape(-1,3)
    return v,f
