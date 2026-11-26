import numpy as np, json, base64
from reg2 import warp
from cl import tosim
from dec import mesh, P
# (nombres Z-Anatomy sin lado, etiqueta, categoría)
S=[('Internal carotid artery','Carótida interna','art'),('Ophthalmic artery','Arteria oftálmica','art'),
   ('Anterior ethmoidal artery','Arteria etmoidal anterior','art'),('Posterior ethmoidal artery','Arteria etmoidal posterior','art'),
   ('Maxillary artery','Arteria maxilar interna','art'),('Descending palatine artery','Arteria palatina descendente','art'),
   ('Artery of pterygoid canal','Arteria vidiana','art'),('Anterior cerebral artery','Arteria cerebral anterior','art'),
   ('Middle cerebral artery (M1-segment)','Arteria cerebral media (M1)','art'),('Basilar artery','Arteria basilar','art'),
   ('Cavernous sinus','Seno cavernoso','ven'),('Anterior intercavernous sinus','Seno intercavernoso anterior','ven'),('Posterior intercavernous sinus','Seno intercavernoso posterior','ven'),
   ('Superior ophthalmic vein','Vena oftálmica superior','ven'),('Inferior ophthalmic vein','Vena oftálmica inferior','ven'),
   ('Optic nerve (II)','Nervio óptico','opt'),('Optic chiasm','Quiasma óptico','opt'),('Optic tract','Cintilla óptica','opt'),
   ('Oculomotor nerve (III)','III par (motor ocular común)','ner'),('Trochlear nerve (IV)','IV par (troclear)','ner'),('Abducens nerve (VI)','VI par (motor ocular externo)','ner'),
   ('Ophthalmic nerve','V1 (nervio oftálmico)','ner'),('Maxillary nerve','V2 (nervio maxilar)','ner'),
   ('Adenohypophysis','Adenohipófisis','gla'),('Neurohypophysis','Neurohipófisis','gla'),
   ('Straight gyrus (Gyrus rectus) · Frontal lobe','Giro recto (lóbulo frontal)','bra'),
   ('Sclera','Globo ocular','eye'),('Cornea','Córnea','eye'),
   ('Medial rectus muscle','Recto medial','mus'),('Inferior rectus muscle','Recto inferior','mus'),('Superior rectus muscle','Recto superior','mus'),
   ('Lateral rectus muscle','Recto lateral','mus'),('Superior oblique muscle','Oblicuo superior','mus'),('Trochlea of superior oblique muscle','Tróclea','mus'),
   ('Inferior oblique muscle','Oblicuo inferior','mus'),('Levator palpebrae superioris','Elevador del párpado','mus'),('Lacrimal gland','Glándula lagrimal','gla2')]
def find(base, side):
    if side: 
        for n in (f'{base} ({side})',):
            if n in P: return n
        # partes con sufijo " · ..."
        if ' · ' in base:
            b,t=base.split(' · '); n=f'{b} ({side}) · {t}'
            if n in P: return n
        return None
    return base if base in P else None
out=[]; total=0
for base,label,cat in S:
    vs=[];fs=[];off=0
    names=[find(base,s) for s in ('right','left')]
    if not any(names): names=[find(base,None)]
    for n in names:
        if not n: continue
        v,f=mesh(n); v=tosim(v); v[:,1]-=1549; w=warp(v)
        keep=(w[:,1]>-12)
        f=f[keep[f].all(1)]
        used=np.unique(f); remap=-np.ones(len(w),int); remap[used]=np.arange(len(used))
        vs.append(w[used]); fs.append(remap[f]+off); off+=len(used)
    if not vs: print('falta',base); continue
    V=np.vstack(vs); Fc=np.vstack(fs)
    assert len(V)<65535
    q=np.round(V*100).astype(np.int16)
    out.append({'n':label,'c':cat,'src':base,'v':base64.b64encode(q.tobytes()).decode(),'i':base64.b64encode(Fc.astype(np.uint16).tobytes()).decode()})
    total+=len(V); print(f'{label:32s} {len(V):6d} v {len(Fc):6d} t  rango y {V[:,1].min():.0f}..{V[:,1].max():.0f} z {V[:,2].min():.0f}..{V[:,2].max():.0f}')
meta={'fuente':'Z-Anatomy (modelo masculino detallado de Human Atlas, github.com/ctzurcanu/human-atlas), derivado de BodyParts3D. Licencia CC BY-SA 4.0.',
      'coordenadas':'mm, espacio del Fantoma 2 ya deformado (x lateral, y cefálico, z anterior); escala 0,01 mm, int16; índices uint16',
      'registro':'dos transformaciones de similitud (órbita/techo etmoidal y esfenoides/silla) mezcladas entre z=WZ(-66) y WZ(-50)',
      'mallas':out}
s=json.dumps(meta,ensure_ascii=False,separators=(',',':'))
open('za_capa.json','w').write(s)
print('total vértices',total,'bytes',len(s))
