document.addEventListener('DOMContentLoaded',function(){
  /* mobile nav toggle */
  var t=document.querySelector('.nav-toggle');
  var u=document.querySelector('nav ul');
  if(t&&u){t.addEventListener('click',function(){u.classList.toggle('open')});}

  /* product category chips (kept for compatibility) */
  var chips=document.querySelectorAll('.chip[data-filter]');
  if(chips.length){
    chips.forEach(function(c){
      c.addEventListener('click',function(){
        chips.forEach(function(x){x.classList.remove('active')});
        c.classList.add('active');
        var v=c.getAttribute('data-filter');
        document.querySelectorAll('[data-cat]').forEach(function(el){
          el.style.display=(v==='all'||el.getAttribute('data-cat')===v)?'':'none';
        });
      });
    });
  }

  /* hero carousel */
  var car=document.querySelector('.hero-carousel');
  if(car){
    var slides=car.querySelectorAll('.slide');
    var dots=car.querySelectorAll('.dot');
    var idx=0,timer=null;
    function go(n){
      idx=(n+slides.length)%slides.length;
      slides.forEach(function(s,i){s.classList.toggle('active',i===idx)});
      dots.forEach(function(d,i){d.classList.toggle('active',i===idx)});
    }
    function play(){timer=setInterval(function(){go(idx+1)},6000);}
    function stop(){if(timer){clearInterval(timer);timer=null;}}
    dots.forEach(function(d,i){d.addEventListener('click',function(){stop();go(i);play();});});
    var prev=car.querySelector('.arrow.prev'),next=car.querySelector('.arrow.next');
    if(prev){prev.addEventListener('click',function(){stop();go(idx-1);play();});}
    if(next){next.addEventListener('click',function(){stop();go(idx+1);play();});}
    car.addEventListener('mouseenter',stop);
    car.addEventListener('mouseleave',play);
    play();
  }

  /* products page: highlight the sidebar link for the visible category */
  var sideLinks=document.querySelectorAll('.side-link');
  if(sideLinks.length){
    var heads=document.querySelectorAll('.product-main .cat-head');
    function sync(){
      var cur='all';
      heads.forEach(function(h){ if(h.getBoundingClientRect().top<=140) cur=h.id; });
      sideLinks.forEach(function(l){l.classList.toggle('active',l.getAttribute('data-side')===cur);});
    }
    window.addEventListener('scroll',sync,{passive:true});
    sync();
  }
});
