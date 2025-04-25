---
layout: page
title: Teaching
permalink: /teaching/
description: 
nav: true
nav_order: 5
---

<style>
/* 背景图片样式 */
.teaching-header {
  width: 100%;
  height: 250px;
  background-image: url('../../assets/teaching/background.jpg');
  background-size: cover;
  background-position: center 80%;
  margin-bottom: 40px;
  border-radius: 8px;
  position: relative;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  margin-top: -20px;
}

/* 引用样式 */
.quote-section {
  position: relative;
  margin: -60px 40px 40px 40px;
  padding: 25px 40px;
  background: var(--global-bg-color);
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  text-align: center;
}

.quote-text {
  font-size: 1.06em;
  line-height: 1.8;
  color: var(--global-text-color);
  font-family: "Playfair Display", "Libre Baskerville", "Georgia", serif;
  font-style: italic;
  margin-bottom: 8px;
  text-align: center;
  max-width: 100%;
  white-space: pre-line;
  display: inline-block;
}

.quote-author {
  text-align: right;
  color: var(--global-text-color-light);
  font-size: 0.9em;
  font-style: normal;
  letter-spacing: 0.02em;
}

.quote-border {
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 4px;
  height: 50%;
  background: var(--global-theme-color);
  border-radius: 2px;
}

.teaching-container {
  margin-bottom: 40px;
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
}

.teaching-list {
  list-style-type: disc;
  padding-left: 1.5em;
}

.teaching-list li {
  position: relative;
  padding-left: 0.5em;
  margin-bottom: 0.3em;
  padding-bottom: 0.2em;
}

.teaching-image {
  width: 250px;
  margin-right: 30px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px var(--global-shadow-color);
  border-radius: 5px;
  transition: all 0.3s ease;
}

.teaching-image:hover {
  transform: scale(1.02);
  box-shadow: 0 3px 6px var(--global-shadow-color);
}

.teaching-content {
  flex: 1;
  min-width: 300px;
}

.teaching-item {
  margin-bottom: 1.5em;
  padding-bottom: 1em;
  border-bottom: 1px dashed rgba(var(--global-theme-color-rgb), 0.1);
  transition: all 0.3s ease;
}

.teaching-container:last-child .teaching-item {
  border-bottom: none;
}

.teaching-course {
  display: block;
  font-weight: 600;
  font-size: 1.2em;
  color: var(--global-text-color);
  margin-bottom: 0.3em;
}

.teaching-semester {
  font-weight: bold;
  color: var(--global-theme-color);
}

.teaching-role {
  font-style: italic;
  margin-left: 0.5em;
}

.teaching-instructor {
  display: block;
  margin-top: 0.3em;
  color: var(--global-text-color-light);
}

.teaching-department {
  display: block;
  color: var(--global-text-color-light);
  margin-top: 0.3em;
}

.teaching-institution {
  display: block;
  color: var(--global-text-color-light);
  font-size: 0.95em;
  margin-top: 0.3em;
}

@media (max-width: 768px) {
  .teaching-container {
    flex-direction: column;
  }
  
  .teaching-image {
    width: 100%;
    max-width: 250px;
    margin-right: 0;
    margin-bottom: 20px;
  }
  
  .quote-section {
    margin: -60px 20px 40px 20px;
    padding: 20px;
  }
  
  .quote-text {
    font-size: 1em;
    line-height: 1.6;
  }
}
</style>

<div class="teaching-header"></div>

<div class="quote-section">
  <div class="quote-border"></div>
  <p class="quote-text">"The mediocre teacher tells. The good teacher explains. The superior teacher demonstrates. The great teacher inspires."</p>
  <p class="quote-author">— William Arthur Ward</p>
</div>


<div class="teaching-container">
  <img src="/assets/teaching/2024-CEE679.png" alt="Teaching CEE 679 AI & Data Science in Transportation 2024" class="teaching-image" loading="lazy">
  
  <div class="teaching-content">
    <div class="teaching-item">
      <span class="teaching-course">CEE 679 AI & Data Science in Transportation</span>
      <div><span class="teaching-semester">Fall 2024</span><span class="teaching-role">(Teaching Assistant)</span></div>
      <span class="teaching-instructor">Instructor: Sikai (Sky) Chen</span>
      <span class="teaching-department">Department of Civil and Environmental Engineering</span>
      <span class="teaching-institution">University of Wisconsin-Madison</span>
    </div>
  </div>
</div>


<div class="teaching-container">
  <img src="/assets/teaching/2023-CEE679.png" alt="Teaching CEE 679 AI & Data Science in Transportation 2023" class="teaching-image" loading="lazy">
  
  <div class="teaching-content">
    <div class="teaching-item">
      <span class="teaching-course">CEE 679 AI & Data Science in Transportation</span>
      <div><span class="teaching-semester">Fall 2023</span><span class="teaching-role">(Teaching Assistant)</span></div>
      <span class="teaching-instructor">Instructor: Sikai (Sky) Chen</span>
      <span class="teaching-department">Department of Civil and Environmental Engineering</span>
      <span class="teaching-institution">University of Wisconsin-Madison</span>
    </div>
  </div>
</div>


<div class="teaching-container">
  <img src="/assets/teaching/2023-CEE370.png" alt="Teaching CEE 370 Transportation Engineering 2023" class="teaching-image" loading="lazy">
  
  <div class="teaching-content">
    <div class="teaching-item">
      <span class="teaching-course">CEE 370 Transportation Engineering</span>
      <div><span class="teaching-semester">Spring 2023</span><span class="teaching-role">(Grader)</span></div>
      <span class="teaching-instructor">Instructor: Soyoung (Sue) Ahn, Sikai (Sky) Chen</span>
      <span class="teaching-department">Department of Civil and Environmental Engineering</span>
      <span class="teaching-institution">University of Wisconsin-Madison</span>
    </div>
  </div>
</div>

<div class="teaching-container">
  <img src="/assets/teaching/2022-CEE370.png" alt="Teaching CEE 370 Transportation Engineering 2022" class="teaching-image" loading="lazy">
  
  <div class="teaching-content">
    <div class="teaching-item">
      <span class="teaching-course">CEE 370 Transportation Engineering</span>
      <div><span class="teaching-semester">Fall 2022</span><span class="teaching-role">(Grader)</span></div>
      <span class="teaching-instructor">Instructor: Soyoung (Sue) Ahn, Sikai (Sky) Chen</span>
      <span class="teaching-department">Department of Civil and Environmental Engineering</span>
      <span class="teaching-institution">University of Wisconsin-Madison</span>
    </div>
  </div>
</div> 