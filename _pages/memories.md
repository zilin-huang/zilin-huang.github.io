---
layout: page
title: Memories
permalink: /memories/
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

<h4 style="text-align: left;">Personal Memories</h4>

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