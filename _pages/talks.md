---
layout: page
title: Talks
permalink: /talks/
description: 
nav: true
nav_order: 7
---

<style>
/* 基础样式 */
.talks-container {
  margin-bottom: 20px;
}

.talks-list {
  list-style-type: disc;
  padding-left: 1.5em;
}

.talks-list li {
  position: relative;
  padding-left: 0.5em;
  margin-bottom: 0.3em;
  padding-bottom: 0.2em;
  border-bottom: none;
}

.talks-list li:last-child {
  border-bottom: none;
}

/* 移除悬停效果 */
.talks-list li:hover {
  background-color: transparent;
  padding-left: 0.5em;
  border-radius: 0;
}

/* 图标样式 */
.talks-list li:before {
  content: none;
}

.invited-talks li:before {
  content: none;
}

.conference-talks li:before {
  content: none;
}

.workshop-talks li:before {
  content: none;
}

.talks-list li:hover:before {
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
.talk-tag {
  display: inline-block;
  font-size: 0.75em;
  padding: 2px 8px;
  margin-right: 8px;
  border-radius: 12px;
  vertical-align: middle;
}

.invited {
  background-color: rgba(33, 150, 243, 0.1);
  color: rgba(33, 150, 243, 0.8);
  border: 1px solid rgba(33, 150, 243, 0.2);
}

.conference {
  background-color: rgba(76, 175, 80, 0.1);
  color: rgba(76, 175, 80, 0.8);
  border: 1px solid rgba(76, 175, 80, 0.2);
}

.workshop {
  background-color: rgba(255, 152, 0, 0.1);
  color: rgba(255, 152, 0, 0.8);
  border: 1px solid rgba(255, 152, 0, 0.2);
}

/* 日期样式 */
.talk-date {
  font-size: 0.9em;
  color: var(--global-text-color-light);
  margin-left: 5px;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .talks-list li {
    padding-left: 2em;
    padding-bottom: 0.8em;
    margin-bottom: 0.8em;
  }
  
  .talks-list li:hover {
    padding-left: 2.2em;
  }
}
</style>

<h4 style="text-align: left;">Invited Talks</h4>

<!-- <div class="talks-container">
  <ul class="talks-list invited-talks">
    <li><span class="talk-tag invited">Invited</span> Title of Invited Talk 1 <span class="talk-date">(Month Year)</span></li>
    <li><span class="talk-tag invited">Invited</span> Title of Invited Talk 2 <span class="talk-date">(Month Year)</span></li>
  </ul>
</div>

<h4 style="text-align: left;">Conference Presentations</h4>

<div class="talks-container">
  <ul class="talks-list conference-talks">
    <li><span class="talk-tag conference">Conference</span> Title of Conference Presentation 1 <span class="talk-date">(Month Year)</span></li>
    <li><span class="talk-tag conference">Conference</span> Title of Conference Presentation 2 <span class="talk-date">(Month Year)</span></li>
  </ul>
</div>

<h4 style="text-align: left;">Workshop Presentations</h4>

<div class="talks-container">
  <ul class="talks-list workshop-talks">
    <li><span class="talk-tag workshop">Workshop</span> Title of Workshop Presentation 1 <span class="talk-date">(Month Year)</span></li>
    <li><span class="talk-tag workshop">Workshop</span> Title of Workshop Presentation 2 <span class="talk-date">(Month Year)</span></li>
  </ul>
</div>  -->