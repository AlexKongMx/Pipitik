const isEnglish=document.documentElement.lang==='en';const menuOpenLabel=isEnglish?'Open menu':'Abrir menú';const menuCloseLabel=isEnglish?'Close menu':'Cerrar menú';
const menu=document.querySelector('.menu-toggle');const nav=document.querySelector('#navigation');
function closeMenu(){menu?.setAttribute('aria-expanded','false');menu?.setAttribute('aria-label',menuOpenLabel);nav?.classList.remove('open')}
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?menuCloseLabel:menuOpenLabel);nav.classList.toggle('open',open)});
nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));document.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu()});window.addEventListener('resize',()=>{if(window.innerWidth>700)closeMenu()});
const dialog=document.querySelector('.lightbox');const photos=[...document.querySelectorAll('[data-photo]')];let trigger;let photoIndex=0;
function showPhoto(index){photoIndex=(index+photos.length)%photos.length;const b=photos[photoIndex];const img=dialog.querySelector('img');img.src=b.dataset.photo;img.alt=b.dataset.alt||b.querySelector('img')?.alt||'';dialog.querySelector('.lightbox-caption').textContent=b.dataset.caption;dialog.querySelector('.lightbox-count').textContent=`${photoIndex+1} / ${photos.length}`;dialog.querySelectorAll('.lightbox-arrow').forEach(a=>a.hidden=photos.length<2)}
photos.forEach((b,index)=>b.addEventListener('click',()=>{trigger=b;showPhoto(index);dialog.showModal();document.body.classList.add('modal-open')}));
dialog?.querySelector('.lightbox-close').addEventListener('click',()=>dialog.close());
dialog?.querySelector('.lightbox-previous').addEventListener('click',()=>showPhoto(photoIndex-1));
dialog?.querySelector('.lightbox-next').addEventListener('click',()=>showPhoto(photoIndex+1));
// Navigate on horizontal swipes without intercepting vertical gestures or pinch zoom.
const viewerImage=dialog?.querySelector('img');let swipeStart=null;
if(viewerImage){
 viewerImage.draggable=false;
 viewerImage.addEventListener('pointerdown',e=>{
  if(!e.isPrimary){swipeStart=null;return}
  if(!dialog.open||photos.length<2||e.button!==0)return;
  swipeStart={id:e.pointerId,x:e.clientX,y:e.clientY};
  viewerImage.setPointerCapture(e.pointerId);
 });
 viewerImage.addEventListener('pointerup',e=>{
  const start=swipeStart;swipeStart=null;
  if(!start||start.id!==e.pointerId||!dialog.open)return;
  const dx=e.clientX-start.x;const dy=e.clientY-start.y;
  if(Math.abs(dx)>=48&&Math.abs(dx)>Math.abs(dy)*1.5)showPhoto(photoIndex+(dx<0?1:-1));
 });
 viewerImage.addEventListener('pointercancel',()=>{swipeStart=null});
 viewerImage.addEventListener('lostpointercapture',()=>{swipeStart=null});
 dialog.addEventListener('close',()=>{swipeStart=null});
}
dialog?.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'||e.key==='ArrowRight'){e.preventDefault();showPhoto(photoIndex+(e.key==='ArrowRight'?1:-1))}});
dialog?.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()}});dialog?.addEventListener('close',()=>{document.body.classList.remove('modal-open');trigger?.focus()});
