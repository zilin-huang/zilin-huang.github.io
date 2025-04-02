---
layout: page
title: Personal
permalink: /personal/
description: 
nav: true
nav_order: 9
---

<style>
/* 基础样式 */
.memories-container {
  margin-bottom: 20px;
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
  background: linear-gradient(to right, var(--global-theme-color), rgba(var(--global-theme-color-rgb), 0.5));
  border-radius: 3px;
}

h5 {
  margin-top: 20px;
  margin-bottom: 15px;
  color: var(--global-text-color);
  font-size: 1.1em;
  font-weight: 500;
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

<h4 style="text-align: left;">Memories</h4>

<!-- <div class="memories-container">
  <ul class="memories-list personal-memories">
    <li><span class="memory-tag personal">Personal</span> Title of Personal Memory 1 <span class="memory-date">(Month Year)</span></li>
    <li><span class="memory-tag personal">Personal</span> Title of Personal Memory 2 <span class="memory-date">(Month Year)</span></li>
  </ul>
</div>

<h4 style="text-align: left;">Travel Memories</h4>

<div class="memories-container">
  <ul class="memories-list travel-memories">
    <li><span class="memory-tag travel">Travel</span> Title of Travel Memory 1 <span class="memory-date">(Month Year)</span></li>
    <li><span class="memory-tag travel">Travel</span> Title of Travel Memory 2 <span class="memory-date">(Month Year)</span></li>
  </ul>
</div>

<h4 style="text-align: left;">Academic Memories</h4>

<div class="memories-container">
  <ul class="memories-list academic-memories">
    <li><span class="memory-tag academic">Academic</span> Title of Academic Memory 1 <span class="memory-date">(Month Year)</span></li>
    <li><span class="memory-tag academic">Academic</span> Title of Academic Memory 2 <span class="memory-date">(Month Year)</span></li>
  </ul>
</div> --> 


<h4 style="text-align: left;">Hobbies</h4>

<div class="honors-container">
  <h5 style="text-align: left;">Basketball</h5>
  <p style="text-align: justify;">
    Basketball has been my favorite sport since elementary school. The rhythm of basketball is like the beating of my heart - constant, energetic, and life-giving. Throughout my basketball journey, I've faced numerous injuries - sprained ankles and scraped knees, but these setbacks never diminished my passion for the game. Basketball has not only strengthened my body but also taught me invaluable lessons about teamwork, perseverance, and rising after every fall.
  </p>
  <p style="text-align: justify;">
    As an avid NBA fan, I've drawn inspiration from legendary players like Allen Iverson, Kobe Bryant, and LeBron James. Their dedication, skill, and impact on the game have deeply influenced my approach to both basketball and life.
  </p>
  
  <h6 style="text-align: left; margin-top: 25px; font-weight: 600;">Basketball Journey</h6>
  
  <!-- Row 1 -->
  <div class="row">
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2023-baksetball-person.jpg" style="width: 100%; height: 200px; object-fit: cover; object-position: center 23%;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2023 Basketball Personal
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2021-baksetball-team-1.jpg" style="width: 100%; height: 200px; object-fit: cover;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2021 Basketball Team Photo
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2021-baksetball-team-2.jpg" style="width: 100%; height: 200px; object-fit: cover;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2021 Basketball Team Photo
      </p>
    </div>
  </div>
  
  <!-- Row 2 -->
  <div class="row mt-2">
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2020-baksetball-team-1.jpg" style="width: 100%; height: 200px; object-fit: cover;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2020 Basketball Team Photo
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <div style="position: relative; height: 200px; overflow: hidden;">
        <video controls style="width: 100%; height: 200px; object-fit: cover;">
          <source src="../assets/personal/basketball/2019-basketball-team-highlights.mp4" type="video/mp4">
          Your browser does not support the video tag.
        </video>
      </div>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2019 Basketball Team Highlights
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2019-baksetball-team.jpg" style="width: 100%; height: 200px; object-fit: cover;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2019 Basketball Team Photo
      </p>
    </div>
  </div>
  
  <!-- Row 3 -->
  <div class="row mt-2">
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2018-baksetball-team-1.jpg" style="width: 100%; height: 200px; object-fit: cover;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2018 Basketball Team Photo
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2018-baksetball-team-2.jpg" style="width: 100%; height: 200px; object-fit: cover; object-position: center bottom;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2018 Basketball Team Photo
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2017-baksetball-team-1.jpg" style="width: 100%; height: 200px; object-fit: cover;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2017 Basketball Team Photo
      </p>
    </div>
  </div>
  
  <!-- Row 4 -->
  <div class="row mt-2">
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2017-baksetball-team-2.jpg" style="width: 100%; height: 200px; object-fit: cover;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2017 Basketball Team Photo
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2016-baksetball-team-1.jpg" style="width: 100%; height: 200px; object-fit: cover; object-position: center 80%;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2016 Basketball Team Action
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2016-baksetball-team-2.jpg" style="width: 100%; height: 200px; object-fit: cover;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2016 Basketball Championship
      </p>
    </div>
  </div>
  
  <!-- Row 5 -->
  <div class="row mt-2">
    <div class="col-md-4 mt-3">
      <div style="position: relative; height: 200px; overflow: hidden;">
        <video controls style="width: 100%; height: 200px; object-fit: cover;">
          <source src="../assets/personal/basketball/2015-baksetball-team-highlights.mp4" type="video/mp4">
          Your browser does not support the video tag.
        </video>
      </div>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2015 Basketball Team Highlights
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2015-baksetball-team.jpg" style="width: 100%; height: 200px; object-fit: cover;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2015 Basketball Team Photo
      </p>
    </div>
    <div class="col-md-4 mt-3">
      <img class="img-fluid rounded z-depth-1" src="../assets/personal/basketball/2014-baksetball-team.jpg" style="width: 100%; height: 200px; object-fit: cover;">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        2014 Basketball Team Photo
      </p>
    </div>
  </div>
</div>