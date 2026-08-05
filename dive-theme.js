/* ===========================================================
   DIVE ENGINE — funções compartilhadas do projeto "Data Diver"
   =========================================================== */

/* ---------- BUBBLES ---------- */
function DiveInitBubbles(containerId, count){
  const field = document.getElementById(containerId);
  if(!field) return;
  for(let i=0;i<count;i++){
    const b = document.createElement('div');
    const size = 6 + Math.random()*22;
    b.className = 'bubble';
    b.style.width = size+'px';
    b.style.height = size+'px';
    b.style.left = (Math.random()*100)+'%';
    b.style.setProperty('--drift', (Math.random()*60-30)+'px');
    b.style.animationDuration = (6+Math.random()*8)+'s';
    b.style.animationDelay = (Math.random()*8)+'s';
    field.appendChild(b);
  }
}

/* ---------- MODULE MAP ---------- */
function DiveInitModuleMap(currentWeek){
  const weeks = [
    {n:21, zn:'Epipelágica', dep:'0-200m'},
    {n:22, zn:'Mesopelágica', dep:'200-1.000m'},
    {n:23, zn:'Batipelágica', dep:'1.000-4.000m'},
    {n:24, zn:'Abissopelágica', dep:'4.000-6.000m'},
    {n:25, zn:'Hadal', dep:'6.000-11.000m'}
  ];
  const map = document.getElementById('moduleMap');
  if(!map) return;
  weeks.forEach(w=>{
    const a = document.createElement('a');
    a.href = 'semana'+w.n+'.html';
    a.className = 'map-node' + (w.n===currentWeek ? ' current' : '') + (w.n<currentWeek ? ' done' : '');
    a.innerHTML = `<div class="dot"></div><div class="num">S${w.n}</div><div class="zn">${w.dep}</div>`;
    map.appendChild(a);
  });
}

/* ---------- DEPTH HUD (scroll tracking) ---------- */
function DiveInitDepthHUD(sections){
  // sections: [{id, label, pct}, ...]
  const depthLabel = document.getElementById('depthLabel');
  const depthFill = document.getElementById('depthFill');
  if(!depthLabel || !depthFill) return;
  const observer = new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
      if(entry.isIntersecting){
        const meta = sections.find(s=>s.id===entry.target.id);
        if(meta){
          depthLabel.textContent = meta.label;
          depthFill.style.width = meta.pct+'%';
        }
      }
    });
  },{threshold:0.4});
  sections.forEach(s=>{
    const el = document.getElementById(s.id);
    if(el) observer.observe(el);
  });
}

/* ---------- XP SYSTEM ---------- */
function DiveCreateXP(maxXP){
  let xp = 0;
  const nowEl = document.getElementById('xpNow');
  const maxEl = document.getElementById('xpMax');
  const finalEl = document.getElementById('xpFinal');
  if(maxEl) maxEl.textContent = maxXP;
  return {
    add(amount){
      xp = Math.min(maxXP, xp + amount);
      if(nowEl) nowEl.textContent = xp;
      if(finalEl) finalEl.textContent = xp;
    },
    get(){ return xp; },
    max(){ return maxXP; }
  };
}

/* ---------- BADGES ---------- */
function DiveCreateBadges(ids){
  const unlocked = {};
  ids.forEach(id=> unlocked[id]=false);
  return {
    unlock(id){
      if(unlocked[id]) return;
      unlocked[id] = true;
      const hudEl = document.getElementById('b'+id);
      const shelfEl = document.getElementById('shelf'+id);
      if(hudEl) hudEl.classList.add('on');
      if(shelfEl) shelfEl.classList.add('on');
    }
  };
}

/* ---------- SINGLE-CHOICE QUIZ ---------- */
function DiveInitQuiz(blockEl, xpSys, correctXP, wrongXP, onDone){
  const opts = blockEl.querySelectorAll('.opt-btn');
  const correctIdx = parseInt(blockEl.querySelector('.options').dataset.correct);
  const fb = blockEl.querySelector('.feedback');
  let answered = false;
  opts.forEach((btn, idx)=>{
    btn.addEventListener('click', ()=>{
      if(answered) return;
      answered = true;
      opts.forEach((b,i)=>{ b.disabled = true; if(i===correctIdx) b.classList.add('correct'); });
      if(idx===correctIdx){
        fb.textContent = '✔ Correto!';
        fb.className = 'feedback ok';
        xpSys.add(correctXP);
      } else {
        btn.classList.add('wrong');
        fb.textContent = '✘ A resposta certa está destacada acima.';
        fb.className = 'feedback bad';
        xpSys.add(wrongXP);
      }
      if(onDone) onDone(idx===correctIdx);
    });
  });
}

/* ---------- TRUE / FALSE LIST ---------- */
function DiveInitTFList(listEl, data, xpSys, correctXP, wrongXP, onAllDone){
  let answeredCount = 0;
  data.forEach(item=>{
    const div = document.createElement('div');
    div.className = 'tf-item';
    div.innerHTML = `
      <p>${item.text}</p>
      <div class="tf-buttons">
        <button class="tf-btn true-btn">Verdadeiro</button>
        <button class="tf-btn false-btn">Mito</button>
      </div>
      <div class="tf-explain">${item.explain}</div>
    `;
    listEl.appendChild(div);
    const trueBtn = div.querySelector('.true-btn');
    const falseBtn = div.querySelector('.false-btn');
    function resolve(pickedTrue){
      trueBtn.disabled = true; falseBtn.disabled = true;
      div.classList.add('answered');
      const correct = (pickedTrue===item.answer);
      const pickedBtn = pickedTrue ? trueBtn : falseBtn;
      pickedBtn.classList.add(correct?'chosen-correct':'chosen-wrong');
      if(!correct){ (item.answer?trueBtn:falseBtn).classList.add('chosen-correct'); }
      xpSys.add(correct?correctXP:wrongXP);
      answeredCount++;
      if(answeredCount===data.length && onAllDone) onAllDone();
    }
    trueBtn.addEventListener('click', ()=>resolve(true));
    falseBtn.addEventListener('click', ()=>resolve(false));
  });
}

/* ---------- CLASSIFY GAME ---------- */
function DiveInitClassify(cardEl, buttons, feedbackEl, progressEl, items, xpSys, correctXP, wrongXP, onAllDone){
  let i = 0;
  function render(){
    if(i>=items.length){
      cardEl.textContent = '✅ Todos os itens classificados!';
      buttons.forEach(b=>b.disabled = true);
      progressEl.textContent = 'Completo';
      if(onAllDone) onAllDone();
      return;
    }
    cardEl.textContent = items[i].label;
    progressEl.textContent = `Item ${i+1} de ${items.length}`;
    feedbackEl.textContent = '';
    buttons.forEach(b=>b.disabled = false);
  }
  buttons.forEach(btn=>{
    btn.addEventListener('click', ()=>{
      if(i>=items.length) return;
      const correct = items[i].cat === btn.dataset.cat;
      if(correct){
        feedbackEl.textContent = '✔ Correto: ' + items[i].cat;
        feedbackEl.style.color = 'var(--bioluminescent)';
        xpSys.add(correctXP);
      } else {
        feedbackEl.textContent = '✘ Era ' + items[i].cat;
        feedbackEl.style.color = 'var(--coral)';
        xpSys.add(wrongXP);
      }
      buttons.forEach(b=>b.disabled = true);
      setTimeout(()=>{ i++; render(); }, 900);
    });
  });
  render();
}

/* ---------- SCENARIOS ---------- */
function DiveInitScenarios(listEl, scenarios, rightLabel, wrongLabel, xpSys, correctXP, wrongXP, onAllDone){
  let answeredCount = 0;
  scenarios.forEach(sc=>{
    const div = document.createElement('div');
    div.className = 'scenario';
    div.innerHTML = `
      <p class="text">${sc.text}</p>
      <div class="scenario-buttons">
        <button class="scenario-btn" data-val="true">${rightLabel}</button>
        <button class="scenario-btn" data-val="false">${wrongLabel}</button>
      </div>
      <div class="scenario-explain">${sc.explain}</div>
    `;
    listEl.appendChild(div);
    const btns = div.querySelectorAll('.scenario-btn');
    btns.forEach(btn=>{
      btn.addEventListener('click', ()=>{
        const picked = btn.dataset.val === 'true';
        const correct = picked === sc.isTrue;
        btns.forEach(b=>b.disabled = true);
        div.classList.add('answered');
        btn.classList.add(correct?'right':'wrongpick');
        if(!correct){
          const rightBtn = [...btns].find(b=> (b.dataset.val==='true')===sc.isTrue);
          rightBtn.classList.add('right');
        }
        xpSys.add(correct?correctXP:wrongXP);
        answeredCount++;
        if(answeredCount===scenarios.length && onAllDone) onAllDone();
      });
    });
  });
}

/* ---------- SEQUENTIAL (BOSS) QUIZ ---------- */
function DiveInitSequentialQuiz(containerEl, progressEl, questions, xpSys, correctXP, wrongXP, xpPerQLabel, onAllDone){
  let idx = 0;
  function render(){
    if(idx >= questions.length){
      container_done();
      return;
    }
    progressEl.textContent = `Pergunta ${idx+1} de ${questions.length}`;
    const item = questions[idx];
    const block = document.createElement('div');
    block.className = 'quiz-block';
    block.innerHTML = `
      <div class="q-label">${xpPerQLabel}</div>
      <h3>${item.q}</h3>
      <div class="options" data-correct="${item.correct}">
        ${item.opts.map(o=>`<button class="opt-btn">${o}</button>`).join('')}
      </div>
      <div class="feedback"></div>
    `;
    containerEl.innerHTML = '';
    containerEl.appendChild(block);
    const opts = block.querySelectorAll('.opt-btn');
    const fb = block.querySelector('.feedback');
    let answered = false;
    opts.forEach((btn, i2)=>{
      btn.addEventListener('click', ()=>{
        if(answered) return;
        answered = true;
        opts.forEach((b,j)=>{ b.disabled = true; if(j===item.correct) b.classList.add('correct'); });
        if(i2===item.correct){
          fb.textContent = '✔ Correto!';
          fb.className = 'feedback ok';
          xpSys.add(correctXP);
        } else {
          btn.classList.add('wrong');
          fb.textContent = '✘ A resposta certa está destacada.';
          fb.className = 'feedback bad';
          xpSys.add(wrongXP);
        }
        setTimeout(()=>{ idx++; render(); }, 1000);
      });
    });
  }
  function container_done(){
    containerEl.innerHTML = '<p style="color:var(--bioluminescent); font-family:var(--font-mono);">🏆 Desafio concluído!</p>';
    progressEl.textContent = 'Completo';
    if(onAllDone) onAllDone();
  }
  render();
}

/* ---------- MISSION CHECKLIST ---------- */
function DiveInitMissionChecklist(listEl, xpSys, xpPerStep){
  const steps = listEl.querySelectorAll('.mission-step');
  steps.forEach(step=>{
    step.addEventListener('click', ()=>{
      if(step.classList.contains('done')) return;
      step.classList.add('done');
      step.querySelector('.check').textContent = '✓';
      xpSys.add(xpPerStep);
    });
  });
}

/* ---------- FINAL RESULT ---------- */
function DiveFinalizeResult(xpSys, rankLabelEl){
  const percent = xpSys.get() / xpSys.max();
  let rank;
  if(percent >= 0.9) rank = '🥇 Cientista de Dados Sênior';
  else if(percent >= 0.7) rank = '🥈 Analista de Big Data';
  else if(percent >= 0.45) rank = '🥉 Explorador em Treinamento';
  else rank = '🔰 Estagiário Curioso';
  rankLabelEl.textContent = rank;
}
