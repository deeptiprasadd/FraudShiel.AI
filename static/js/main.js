// Hero CTA ripple (nice click effect)
document.addEventListener("click", (e) => {
  const btn = e.target.closest(".hero-cta");
  if (!btn) return;
  const r = btn.getBoundingClientRect();
  btn.style.setProperty("--click-x", `${e.clientX - r.left}px`);
  btn.style.setProperty("--click-y", `${e.clientY - r.top}px`);
});

// Neural lines animation (lightweight)
function heroParticles() {
  const canvas = document.getElementById("heroCanvas");
  if (!canvas) return;

  const parent = canvas.parentElement;
  const ctx = canvas.getContext("2d");

  function resize(){
    canvas.width = parent.clientWidth;
    canvas.height = parent.clientHeight;
  }
  resize(); addEventListener("resize", resize);

  const N = 80;
  const nodes = Array.from({length:N}, ()=>({
    x: Math.random()*canvas.width,
    y: Math.random()*canvas.height,
    vx:(Math.random()-0.5)*0.7,
    vy:(Math.random()-0.5)*0.7
  }));

  function frame(){
    ctx.clearRect(0,0,canvas.width, canvas.height);
    // lines
    for(let i=0;i<N;i++){
      for(let j=i+1;j<N;j++){
        const a=nodes[i], b=nodes[j];
        const dx=a.x-b.x, dy=a.y-b.y, d=Math.hypot(dx,dy);
        if(d<160){
          ctx.strokeStyle = `rgba(39,194,255, ${1-d/160})`;
          ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke();
        }
      }
    }
    // points
    nodes.forEach(n=>{
      n.x+=n.vx; n.y+=n.vy;
      if(n.x<0||n.x>canvas.width) n.vx*=-1;
      if(n.y<0||n.y>canvas.height) n.vy*=-1;
      ctx.fillStyle="rgba(39,194,255,.9)";
      ctx.beginPath(); ctx.arc(n.x,n.y,2.4,0,Math.PI*2); ctx.fill();
    });

    requestAnimationFrame(frame);
  }
  frame();
}
document.addEventListener("DOMContentLoaded", heroParticles);
