---
layout: page
title: Personal
permalink: /personal/
description: 
nav: true
nav_order: 10
---

<style>
/* 基础样式 */
.memories-container {
  margin-bottom: 20px;
}

/* 添加导航栏样式 */
.section-nav {
  position: fixed;
  left: 40px;
  top: 50%;
  transform: translateY(-50%);
  background-color: white;
  padding: 15px;
  border-radius: 12px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  border: 1px solid rgba(var(--global-theme-color-rgb), 0.15);
}

.section-nav a {
  display: block;
  padding: 8px 25px;
  margin: 6px 0;
  color: var(--global-theme-color);
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.2s ease;
  font-size: 1em;
  text-align: center;
  position: relative;
  background-color: transparent;
}

.section-nav a:hover {
  background-color: rgba(var(--global-theme-color-rgb), 0.1);
}

.section-nav a.active {
  background-color: var(--global-theme-color);
  color: white;
  font-weight: 500;
}

@media (max-width: 768px) {
  .section-nav {
    display: none;
  }
}

.memories-list {
  list-style-type: disc;
  padding-left: 1.5em;
}

.memories-list li {
  position: relative;
  padding-left: 0.5em;
  margin-bottom: 0.3em;
  padding-bottom: 0.2em;
  border-bottom: none;
}

.memories-list li:last-child {
  border-bottom: none;
}

/* 移除悬停效果 */
.memories-list li:hover {
  background-color: transparent;
  padding-left: 0.5em;
  border-radius: 0;
}

/* 图标样式 */
.memories-list li:before {
  content: none;
}

.personal-memories li:before {
  content: none;
}

.travel-memories li:before {
  content: none;
}

.academic-memories li:before {
  content: none;
}

.memories-list li:hover:before {
  transform: none;
}

/* 标题样式 */
h4 {
  position: relative;
  padding-bottom: 10px;
  margin-bottom: 20px;
  margin-top: 40px;
  color: var(--global-text-color);
  font-size: 1.3em;
  font-weight: 600;
}

h4:first-of-type {
  margin-top: 0;
}

h4:after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 50px;
  height: 3px;
  background: var(--global-theme-color);
  border-radius: 3px;
}

h5 {
  margin-top: 5px;
  margin-bottom: 10px;
  color: var(--global-text-color);
  font-size: 1.05em;
  font-weight: 600;
  padding-left: 0;
  border-left: none;
  position: relative;
  display: inline-block;
  background: linear-gradient(120deg, rgba(33, 150, 243, 0.12), rgba(3, 169, 244, 0.05));
  padding: 5px 12px;
  border-radius: 8px;
  border: 1px solid rgba(33, 150, 243, 0.15);
  box-shadow: 0 2px 4px rgba(33, 150, 243, 0.05);
  transition: all 0.3s ease;
}

h5:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(33, 150, 243, 0.1);
  background: linear-gradient(120deg, rgba(33, 150, 243, 0.18), rgba(3, 169, 244, 0.08));
}

/* 标签样式 */
.memory-tag {
  display: inline-block;
  font-size: 0.75em;
  padding: 2px 8px;
  margin-right: 8px;
  border-radius: 12px;
  vertical-align: middle;
}

.personal {
  background-color: rgba(33, 150, 243, 0.1);
  color: rgba(33, 150, 243, 0.8);
  border: 1px solid rgba(33, 150, 243, 0.2);
}

.travel {
  background-color: rgba(76, 175, 80, 0.1);
  color: rgba(76, 175, 80, 0.8);
  border: 1px solid rgba(76, 175, 80, 0.2);
}

.academic {
  background-color: rgba(255, 152, 0, 0.1);
  color: rgba(255, 152, 0, 0.8);
  border: 1px solid rgba(255, 152, 0, 0.2);
}

/* 日期样式 */
.memory-date {
  font-size: 0.9em;
  color: var(--global-text-color-light);
  margin-left: 5px;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .memories-list li {
    padding-left: 2em;
    padding-bottom: 0.8em;
    margin-bottom: 0.8em;
  }
  
  .memories-list li:hover {
    padding-left: 2.2em;
  }
}
</style>

<!-- Section navigation sidebar -->
<div class="section-nav">
  <a href="#memories">Memories</a>
  <a href="#hobbies">Hobbies</a>
</div>

<h4 id="memories" style="text-align: left;">Memories</h4>



<h4 id="memories" style="text-align: left;">Leadership</h4>



<!-- <h4 id="volunteering" style="text-align: left;">Volunteering</h4>

<p style="text-align: justify;">
  I believe in the power of volunteering to create positive change in our communities. Throughout my academic journey, I've been actively involved in various community service initiatives that have not only made a difference in people's lives but have also shaped my perspective on social responsibility and leadership.
</p> -->


<h4 id="hobbies" style="text-align: left;">Hobbies</h4>

<div class="honors-container">
  <h5 style="text-align: left;">Chef</h5>
  <p style="text-align: justify;">
    Cooking has become one of my greatest passions in recent years. I specialize in Cantonese cuisine, particularly in making soups, pan-frying steaks, and preparing salmon. Honestly, I didn't know how to cook before coming to the USA. But gradually, I discovered the joy of cooking. It helps me relax and unwind after intense research work, providing a balance to the mental demands of academic life. Now, cooking has become a way for me to understand different cultures through their cuisines. I believe that good food has the power to bring people together and create lasting memories.
  </p>

  <!-- Row 1 -->
  <div class="row">
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/chef/2025-chef-1.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Chef Huang (黄小厨) 
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/chef/2025-chef-2.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        ‌Chicken Clay Pot‌ (啫啫鸡煲)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/chef/2025-chef-3.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Seafood Tofu Clay Pot (海鲜豆腐煲)
      </p>
    </div>
  </div>
  
  <!-- Row 2 -->
  <div class="row mt-1">
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/chef/2025-chef-4.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Beef Clay Pot (牛肉煲)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/chef/2025-chef-5.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Fish-Fragrant Eggplant Clay Pot (鱼香茄子煲)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/chef/2025-chef-6.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Beef Brisket Clay Pot (牛腩煲)
      </p>
    </div>
  </div>


  <h5 style="text-align: left;">Basketball</h5>
  <p style="text-align: justify;">
    As an avid NBA fan, my first jersey was <strong>Ming Yao</strong>'s Houston Rockets uniform. During high school, I would purchase <i>Slam Dunk</i> magazine every week. <strong>LeBron</strong> has probably had the most profound impact on me. And, <strong>Kobe</strong>'s "Mamba Mentality" has deeply influenced my way of dealing with challenges. I was fortunate enough to live in Wisconsin, where Chinese basketball star <strong>Jianlian Yi</strong> played for the Milwaukee Bucks. I remember how happy I was the day he was drafted by Milwaukee. Also, Giannis Antetokounmpo's basketball journey deeply touched me—from a skinny kid to an NBA champion.
  </p>

  <p style="text-align: justify;">
    I've been injured many times in my basketball journey, such as sprained ankles and scraped knees. The most severe setback occurred in early 2024 when I suffered a lower back injury requiring surgery. For the first two weeks, I was essentially immobile, confined to bed rest. However, these challenges never diminished my passion for the game. As <strong>Iverson</strong> famously said, "What doesn't kill you makes you stronger." Basketball has not only strengthened my body but also taught me invaluable life lessons about teamwork, perseverance, and rising after every fall.
  </p>
  
  <!-- Row 1 -->
  <div class="row">
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2023-baksetball-person.jpg" style="width: 100%; height: 200px; object-fit: cover; object-position: center 23%;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Bakke Gym, UW-Madison (2023)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2021-baksetball-team-2.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2021)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2020-baksetball-team-1.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2020)
      </p>
    </div>
  </div>
  
  <!-- Row 2 -->
  <div class="row mt-1">
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2019-baksetball-team.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2019)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <div style="position: relative; height: 200px; overflow: hidden;">
        <video controls style="width: 100%; height: 200px; object-fit: cover;">
          <source src="../assets/personal/basketball/2018-basketball-team-highlights.mp4" type="video/mp4">
          Your browser does not support the video tag.
        </video>
      </div>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Highlights (2018)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2018-baksetball-team-0.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2018)
      </p>
    </div>
  </div>
  
  <!-- Row 3 -->
  <div class="row mt-1">
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2018-baksetball-team-2.jpg" style="width: 100%; height: 200px; object-fit: cover; object-position: center bottom;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2018)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2018-baksetball-team-1.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2018)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2017-baksetball-team-1.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2017)
      </p>
    </div>
  </div>
  
  <!-- Row 4 -->
  <div class="row mt-1">
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2017-baksetball-team-2.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2017)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2016-baksetball-team-1.jpg" style="width: 100%; height: 200px; object-fit: cover; object-position: center 80%;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2016)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2016-baksetball-team-2.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2016)
      </p>
    </div>
  </div>
  
  <!-- Row 5 -->
  <div class="row mt-1">
    <div class="col-md-4 mt-3">
      <div style="position: relative; height: 200px; overflow: hidden;">
        <video controls style="width: 100%; height: 200px; object-fit: cover;">
          <source src="../assets/personal/basketball/2015-baksetball-team-highlights.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
      </div>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Highlights (2015)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2015-baksetball-team.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2015)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2014-baksetball-team.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Basketball Team Photo (2014)
      </p>
    </div>
  </div>
  


  <!-- <h5 style="text-align: left;">Photography</h5>
  <p style="text-align: justify;">
    I have a deep passion for photography, specializing in documentary and journalistic photography. My philosophy is: "A photograph is a witness to a moment in history." My journey in photography began with a Nikon D700, followed by a Canon 70D, and later a Canon 6D. I served as the vice president of the photography association, and regularly contributed photos to the university's official website. I am a photographer for Visual China and a member of the Guangzhou Photography Association. I also have developed an interest in astrophotography and I am a member of the Astronomy Club. This is a collection of postcards I created from my photography work <a href="{{ '/photographic_works/postcards/' | relative_url }}">here</a>. 
  </p>
  
  <p style="text-align: justify;">
    During my university years, I co-founded a creative media studio with senior students, focusing on MG animation and micro-film production. Our studio's original character "Zuiyao B (最耀B)" garnered over 100 million views across platforms. You can find our works on <a href="https://www.youtube.com/playlist?list=PLnQTmrTdfHskys9PPoE_mWQStAVr59GtY" target="_blank">YouTube</a> and <a href="https://space.bilibili.com/26055201" target="_blank">Bilibili</a>. Additionally, my micro-film "Drinking Water and Remembering the Source (饮水思源)" won the "Best Film Silver Award" (RMB ¥40,000) <a href="{{ '/assets/personal/Photography/2016-movie-award.png' | relative_url }}" target="_blank">[Certificate]</a>. I'm particularly proud of my role as executive producer in the university commemorative graduation video <a href="https://v.qq.com/x/page/k0702zufnaj.html" target="_blank">"The Journey (走过)"</a>.
  </p> -->
  
  <!-- Photography images -->
  <!-- <div class="row">
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/Photography/2018-photography.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Astrophotography Activities (2018)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/Photography/2016-photography1.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Photography Activities (2016)
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/Photography/2014-photography.jpg" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        The camera I own (2014)
      </p>
    </div>
  </div>

  <h5 style="text-align: left;">Arts</h5>
  <p style="text-align: justify;">
    Art has always been an integral part of my life, manifesting in various forms. I have a deep appreciation for fine arts and frequently visit art museums and galleries to immerse myself in different artistic expressions and cultural narratives. As a member of the Calligraphy Association, I practice Chinese calligraphy, which I find to be a meditative art form that connects traditional aesthetics with personal expression.
  </p>

  <p style="text-align: justify;">
    Music is another passion of mine, with eclectic tastes spanning multiple genres. I particularly enjoy R&B for its soulful expressions, classical music for its complexity and emotional depth, and British rock for its innovative spirit and cultural impact. In the Mandarin music scene, I deeply admire Jay Chou for his unique ability to blend Chinese traditional elements with modern musical styles, creating a distinctive sound that bridges cultural gaps while maintaining artistic integrity.
  </p>

</div> -->

<script>
document.addEventListener('DOMContentLoaded', function() {
  const sectionLinks = document.querySelectorAll('.section-nav a');
  
  // Set first section as active by default
  sectionLinks[0].classList.add('active');
  
  // Update active state on scroll
  function updateActiveSection() {
    const scrollPosition = window.scrollY;
    const sections = document.querySelectorAll('h4[id]');
    
    sections.forEach((section, index) => {
      const sectionTop = section.offsetTop - 100;
      const sectionBottom = sectionTop + section.offsetHeight;
      
      if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
        sectionLinks.forEach(link => link.classList.remove('active'));
        sectionLinks[index].classList.add('active');
      }
    });
  }
  
  // Update active state on click
  sectionLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      sectionLinks.forEach(l => l.classList.remove('active'));
      e.target.classList.add('active');
    });
  });
  
  window.addEventListener('scroll', updateActiveSection);
  updateActiveSection();
});
</script>



