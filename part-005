(() => {
  'use strict';
  const content=window.portfolioContent;
  if(!content)return;
  const grid=document.getElementById('project-grid');
  const filters=document.querySelector('.filters');
  const count=document.querySelector('.project-count');
  const dialog=document.getElementById('project-dialog');
  let lastTrigger=null;
  const categories=['Todos','Marca / packaging','Campañas','Animación','Modelado 3D','Visualización de datos'];
  const make=(tag,className,text)=>{const el=document.createElement(tag);if(className)el.className=className;if(text!==undefined)el.textContent=text;return el;};
  const safeAsset=(value)=>typeof value==='string'&&!/^(javascript|data|vbscript):/i.test(value.trim())?value:null;
  const escapeId=(id)=>encodeURIComponent(id);
  const assetUrl=(path)=>window.portfolioAssetUrl?window.portfolioAssetUrl(path):path;
  function emphasized(tag,className,value,phrases=[]){
    const el=make(tag,className);let cursor=0;
    const highlights=phrases.filter(phrase=>typeof phrase==='string'&&phrase.length);
    while(cursor<value.length){
      const next=highlights.map(phrase=>({phrase,index:value.indexOf(phrase,cursor)})).filter(match=>match.index>=0).sort((a,b)=>a.index-b.index||b.phrase.length-a.phrase.length)[0];
      if(!next){el.append(document.createTextNode(value.slice(cursor)));break;}
      el.append(document.createTextNode(value.slice(cursor,next.index)),make('strong','',next.phrase));cursor=next.index+next.phrase.length;
    }
    return el;
  }
  function projectCover(project,className){
    const wrapper=make('div',className);
    if(project.pendingMedia||!safeAsset(project.image)){
      wrapper.classList.add('pending-cover');
      wrapper.append(make('span','pending-wordmark','RAID'),make('span','pending-media-label','Imágenes por añadir'));
      return wrapper;
    }
    const image=make('img');image.src=project.image;image.alt=project.isSample?`Composición de muestra para ${project.category}`:project.imageAlt||project.title;
    image.loading='lazy';image.width=800;image.height=600;
    if(project.imageFit==='contain')wrapper.classList.add('cover-contain');
    if(project.coverStyle==='illustration')wrapper.classList.add('illustration-cover');
    wrapper.append(image);
    if(project.gallery?.some(item=>item.type==='video')){const play=make('span','video-cover-label','▶ Ver video');play.setAttribute('aria-hidden','true');wrapper.classList.add('video-cover');wrapper.append(play);}
    return wrapper;
  }
  function manualLink(project,className,label){
    const link=make('a',className,label||project.pdfLabel||'Ver manual completo');
    link.href=project.pdf;link.target='_blank';link.rel='noopener noreferrer';
    return link;
  }
  function softwareList(project){
    if(!project.software?.length)return null;
    const list=make('ul','software-list');list.setAttribute('aria-label','Programas utilizados');
    const icons=content.softwareIcons||{};
    for(const name of project.software){
      const item=make('li');
      if(icons[name]){const icon=make('img');icon.src=icons[name];icon.alt='';icon.width=28;icon.height=28;item.append(icon);}
      item.append(make('span','',name));list.append(item);
    }
    return list;
  }
  function hasProjectUrl(project){
    try{return ['https:','http:'].includes(new URL(project.url).protocol);}catch{return false;}
  }
  function liveProjectLink(project,className){
    const link=make('a',className,`${project.urlLabel||'Visitar sitio'} ↗`);
    link.href=project.url;link.target='_blank';link.rel='noopener noreferrer';return link;
  }

  document.querySelectorAll('.section-strip').forEach(strip=>{
    const track=make('div','strip-track');
    for(let copy=0;copy<2;copy++){
      const group=make('div','strip-group');
      for(let repeat=0;repeat<4;repeat++){
        group.append(make('span','strip-name',strip.dataset.stripLabel),make('span','strip-star','✳'));
      }
      track.append(group);
    }
    strip.append(track);
  });
  const reducedMotion=matchMedia('(prefers-reduced-motion: reduce)');
  const motionToggle=document.querySelector('.motion-toggle');
  let motionPaused=false;
  function renderMotion(){
    const paused=motionPaused||reducedMotion.matches;
    document.documentElement.classList.toggle('motion-paused',paused);
    motionToggle.setAttribute('aria-pressed',String(paused));
    motionToggle.textContent=paused?'Activar animaciones ▷':'Pausar animaciones Ⅱ';
    if(reducedMotion.matches){motionToggle.disabled=true;motionToggle.textContent='Movimiento reducido';}
    else motionToggle.disabled=false;
  }
  motionToggle.addEventListener('click',()=>{motionPaused=!motionPaused;renderMotion();});
  reducedMotion.addEventListener('change',renderMotion);renderMotion();
  const cards=[];
  const categorySections=new Map();
  categories.slice(1).forEach((category,index)=>{
    const projects=content.projects.filter(p=>p.category===category);if(!projects.length)return;
    const section=make('section','project-category-section');section.dataset.category=category;
    const titleId=`project-category-${index+1}`;section.setAttribute('aria-labelledby',titleId);
    const header=make('div','category-heading');const title=make('h3','',category);title.id=titleId;
    const total=projects.filter(p=>!p.isSample).length;
    header.append(title,make('span','category-total',total?`${String(total).padStart(2,'0')} ${total===1?'proyecto':'proyectos'}`:'Próximamente'));
    const projectGrid=make('div','project-grid');if(projects.length===2)projectGrid.classList.add('two-projects');
    section.append(header,projectGrid);grid.append(section);categorySections.set(category,{section,grid:projectGrid});
  });
  content.projects.forEach((project,index)=>{
    const card=make('article','project-card');card.dataset.category=project.category;
    const trigger=make('button','project-trigger');trigger.type='button';trigger.setAttribute('aria-haspopup','dialog');trigger.setAttribute('aria-label',`${project.isSample?'Ver muestra de':'Abrir proyecto:'} ${project.title}`);
    const art=projectCover(project,'project-image');
    const info=make('div','project-info');const titles=make('div');titles.append(make('span','project-category',`${String(index+1).padStart(2,'0')} / ${project.category.toUpperCase()}`),make('h4','',project.title));const arrow=make('span','project-arrow','↗');arrow.setAttribute('aria-hidden','true');info.append(titles,arrow);trigger.append(art,info);
    if(project.summary)trigger.append(emphasized('p','project-description',project.summary,project.summaryEmphasis));
    card.append(trigger);
    const software=softwareList(project);if(software){const meta=make('div','project-software');meta.append(software);card.append(meta);}
    if(safeAsset(project.pdf)){
      const actions=make('div','project-card-actions');actions.append(manualLink(project,'project-manual-link','Ver manual completo · PDF ↗'));card.append(actions);
    }
    if(hasProjectUrl(project)){const actions=make('div','project-card-actions');actions.append(liveProjectLink(project,'project-manual-link'));card.append(actions);}
    if(project.isSample)card.append(make('span','sample-badge','MUESTRA / PROYECTO PENDIENTE'));
    trigger.addEventListener('click',()=>openProject(project,trigger));
    categorySections.get(project.category).grid.append(card);cards.push(card);
  });
  const filterButtons=categories.map(category=>{
    const button=make('button','filter',category);button.type='button';button.setAttribute('aria-pressed',String(category==='Todos'));
    button.addEventListener('click',()=>{
      filterButtons.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
      const visible=[];
      cards.forEach((card,index)=>{const show=category==='Todos'||card.dataset.category===category;card.hidden=!show;if(show){visible.push(content.projects[index]);card.style.animation='none';void card.offsetWidth;card.style.animation='';}});
      categorySections.forEach(({section},name)=>{section.hidden=category!=='Todos'&&category!==name;});
      updateCount(visible);document.querySelector('.empty-state').hidden=visible.length!==0;
    });filters.append(button);return button;
  });
  function updateCount(projects){
    const real=projects.filter(p=>!p.isSample).length,samples=projects.length-real;
    const labels=[];
    if(real)labels.push(`${String(real).padStart(2,'0')} ${real===1?'PROYECTO':'PROYECTOS'}`);
    if(samples)labels.push(`${String(samples).padStart(2,'0')} ${samples===1?'MUESTRA':'MUESTRAS'}`);
    count.textContent=labels.join(' · ')||'00 PROYECTOS';
  }
  updateCount(content.projects);


  function openProject(project,trigger){
    lastTrigger=trigger;
    const target=document.querySelector('.dialog-content');target.replaceChildren();
    const body=make('div','dialog-body');body.append(make('p','dialog-category',[project.category,project.type].filter(Boolean).join(' / ').toUpperCase()));
    const title=make('h2','',project.title);title.id='dialog-title';body.append(title);
    const description=project.description||(project.isSample?'Esta composición es una vista de muestra de la categoría. Aquí se incorporará un proyecto real, con sus imágenes, contexto y proceso.':'Proyecto de portafolio.');
    description.split(/\n\n+/).forEach(paragraph=>body.append(emphasized('p','dialog-intro',paragraph,project.descriptionEmphasis)));
    const software=softwareList(project);if(software){const tools=make('div','dialog-software');tools.append(make('p','software-heading','Programas utilizados'),software);body.append(tools);}
    if(safeAsset(project.pdf)){
      const actions=make('div','dialog-actions');actions.append(manualLink(project,'button button-primary','Ver manual completo ↗'));
      const download=manualLink(project,'button button-secondary','Descargar PDF ↓');download.download=project.pdfName||'manual.pdf';actions.append(download);body.append(actions);
    }
    if(hasProjectUrl(project)){const actions=make('div','dialog-actions');actions.append(liveProjectLink(project,'button button-primary'));body.append(actions);}
    if(project.pendingMedia)body.append(make('p','project-media-pending','Las imágenes de este proyecto se añadirán próximamente.'));
    const facts=make('div','dialog-facts');
    [['Contexto',project.context],['Objetivo',project.objective],['Mi participación',project.role],['Proceso',project.process],['Resultado',project.result]].forEach(([label,text])=>{if(text||project.isSample){const fact=make('section','dialog-fact');fact.append(make('h3','',label),make('p','',text||'Información del proyecto por incorporar.'));facts.append(fact);}});
    body.append(facts);
    if(Array.isArray(project.gallery)&&project.gallery.length){
      const gallery=make('div','dialog-gallery');
      for(const item of project.gallery){
        const path=safeAsset(typeof item==='string'?item:item.src);if(!path)continue;
        const figure=make('figure','project-gallery-figure');
        if(item.layout==='portrait')figure.classList.add('portrait-piece');
        if(item.layout==='illustration')figure.classList.add('illustration-piece');
        const media=make(item.type==='video'?'video':'img');const mediaUrl=assetUrl(path);media.src=mediaUrl;
        if(media.tagName==='VIDEO'){
          media.controls=true;media.playsInline=true;media.preload='none';
          if(item.width&&item.height){media.width=item.width;media.height=item.height;}
          if(safeAsset(item.poster))media.poster=assetUrl(item.poster);
          media.setAttribute('aria-label',item.caption||project.title);
          const fallback=make('a','','Abrir video');fallback.href=mediaUrl;media.append(fallback);
          figure.classList.add('video-piece');
        }else{media.alt=item.alt||project.title;media.loading='lazy';}
        figure.append(media);
        const caption=make('figcaption');caption.append(make('span','',item.caption||project.title));
        const original=make('a','gallery-original-link',media.tagName==='VIDEO'?'Abrir video completo ↗':'Abrir imagen completa ↗');original.href=mediaUrl;original.target='_blank';original.rel='noopener noreferrer';caption.append(original);figure.append(caption);gallery.append(figure);
      }
      body.append(gallery);
    }else if(!project.pendingMedia)body.append(projectCover(project,'dialog-fallback-cover'));
    if(project.showBehance!==false){const link=make('a','button button-secondary','Ver mi Behance ↗');link.href='https://www.behance.net/octaviorojas7';link.target='_blank';link.rel='noopener noreferrer';body.append(link);}target.append(body);
    dialog.showModal();document.body.classList.add('dialog-open');dialog.scrollTop=0;
    history.replaceState(null,'',`#proyecto-${escapeId(project.id)}`);
  }
  function closeProject(){dialog.close();}
  dialog.querySelector('.dialog-close').addEventListener('click',closeProject);
  dialog.addEventListener('click',event=>{if(event.target===dialog){const rect=dialog.getBoundingClientRect();if(event.clientX<rect.left||event.clientX>rect.right||event.clientY<rect.top||event.clientY>rect.bottom)closeProject();}});
  dialog.addEventListener('close',()=>{document.body.classList.remove('dialog-open');dialog.querySelectorAll('video').forEach(v=>v.pause());history.replaceState(null,'','#proyectos');lastTrigger?.focus({preventScroll:true});});

  const menuToggle=document.querySelector('.menu-toggle');const nav=document.getElementById('main-nav');
  function closeMenu(){menuToggle.setAttribute('aria-expanded','false');nav.classList.remove('open');}
  menuToggle.addEventListener('click',()=>{const open=menuToggle.getAttribute('aria-expanded')!=='true';menuToggle.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);});
  nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){closeMenu();menuToggle.focus();}});
  document.addEventListener('click',e=>{if(!e.target.closest('.site-header'))closeMenu();});
  const mobile=matchMedia('(max-width:760px)');mobile.addEventListener('change',()=>closeMenu());

  const sections=[...document.querySelectorAll('main > section[id]')];
  const navLinks=[...nav.querySelectorAll('a')];let ticking=false;
  function updateNavigation(){let current=sections[0];const edge=innerHeight*.38;for(const section of sections)if(section.getBoundingClientRect().top<=edge)current=section;navLinks.forEach(a=>{if(a.hash===`#${current.id}`)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});document.getElementById('current-section').textContent=current.dataset.section||'INICIO';ticking=false;}
  addEventListener('scroll',()=>{if(!ticking){ticking=true;requestAnimationFrame(updateNavigation);}},{passive:true});updateNavigation();
  if('IntersectionObserver'in window){
    const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible','in-view');observer.unobserve(entry.target);}});},{threshold:.08});
    document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
    const stripsObserver=new IntersectionObserver(entries=>{entries.forEach(entry=>entry.target.classList.toggle('strip-running',entry.isIntersecting));},{threshold:0});
    document.querySelectorAll('.section-strip').forEach(el=>stripsObserver.observe(el));
    document.documentElement.classList.add('js-motion');
  }
  if(location.hash.startsWith('#proyecto-')){const id=decodeURIComponent(location.hash.slice(10));const project=content.projects.find(p=>p.id===id);if(project){const index=content.projects.indexOf(project);openProject(project,cards[index].querySelector('button'));}}
})();
