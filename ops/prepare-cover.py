from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter,ImageEnhance
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
original=Image.open(ROOT/'public/assets/14rXf3nOjN4UfxEK78OU2vr5zWIweORDb.webp').convert('RGB').crop((0,150,1440,1590))
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--background',required=True);args=parser.parse_args()
background=Image.open(args.background).convert('RGB').resize((3360,1440))
h,w=1440,3360
x=np.arange(w,dtype=float);sx=np.clip(1500+(x-1050)*.8,0,3359)
source_marks=[np.full(w,-1000.),444-.195*sx,758-.022*sx,971+.017*sx,np.full(w,1100.),np.full(w,1439.)]
target_marks=[np.full(w,-1000.),281-.18*x,659-.0476*x,834+.029*x,np.full(w,1040.),np.full(w,1439.)]
# Match the original wall stripes before compositing; no source subjects are regenerated.
from scipy.ndimage import map_coordinates
sy=np.empty((h,w))
for col in range(w):
 a=np.array([v[col] for v in target_marks]);b=np.array([v[col] for v in source_marks]);sy[:,col]=np.interp(np.arange(h),a,b)
sxx=np.broadcast_to(sx,(h,w));arr=np.asarray(background).astype(float)
warped=np.stack([map_coordinates(arr[:,:,c],[sy,sxx],order=1,mode='nearest') for c in range(3)],axis=2)
# Neutralize the AI background to match the original plaster wall.
from scipy.ndimage import gaussian_filter
orig=np.asarray(original).astype(float);yy,xx=np.indices(orig.shape[:2]);wall=(xx>900)&(yy>90)&(yy<1040)&(orig.min(axis=2)>95)&((orig.max(axis=2)-orig.min(axis=2))<34)
coords=np.column_stack([np.ones(wall.sum()),xx[wall]/1440,yy[wall]/1440,(xx[wall]/1440)*(yy[wall]/1440)])
wy,wx=np.indices((h,w));plane=np.stack([np.ones((h,w)),np.minimum(wx,1430)/1440,wy/1440,np.minimum(wx,1430)*wy/(1440*1440)],axis=2)
for c in range(3):
 coef=np.linalg.lstsq(coords,orig[:,:,c][wall],rcond=None)[0];tone=plane@coef;current=gaussian_filter(warped[:,:,c],sigma=80);blend=np.clip((1050-wy)/120,0,1);warped[:,:,c]*=(tone/current)*blend+(1-blend)
warped=np.clip(warped,0,255)
canvas=Image.fromarray(warped.astype('uint8'));canvas.paste(original,(0,0))
mask=Image.new('L',(w,h),0);d=ImageDraw.Draw(mask)
d.polygon([(1140,420),(1290,450),(1370,530),(1385,800),(1395,1370),(1250,1380),(1190,1170),(1110,1300),(1020,1300),(1050,1180),(1090,1100),(1090,850),(1060,680),(1100,530)],fill=255)
d.rectangle((1390,0,w-1,h-1),fill=255)
d.rectangle((1080,1290,1440,h-1),fill=255)
d.rectangle((1130,1170,1440,h-1),fill=255)
mask=mask.filter(ImageFilter.GaussianBlur(8))
canvas=Image.composite(Image.fromarray(warped.astype('uint8')),canvas,mask)
canvas=ImageEnhance.Contrast(canvas).enhance(1.09);canvas=ImageEnhance.Color(canvas).enhance(1.08)
a=np.asarray(canvas).astype(float);a[:,:,0]*=1.018;a[:,:,2]*=.98;canvas=Image.fromarray(np.clip(a,0,255).astype('uint8'))
canvas.resize((2520,1080),Image.Resampling.LANCZOS).save(ROOT/'public/assets/studio-cover-panorama-fal.webp',quality=88,method=6)
canvas.crop((0,0,1800,1440)).resize((1350,1080),Image.Resampling.LANCZOS).save(ROOT/'public/assets/studio-cover-mobile-fal.webp',quality=88,method=6)
canvas.resize((1680,720)).save('/workspace/scratch/6aabbbf34429/cover-composite-review.jpg',quality=94)
print('Saved original-subject composite with AI workshop background; 2520x1080 and 1350x1080.')
