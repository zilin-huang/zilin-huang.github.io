---
layout: page
title: Talks
permalink: /talks/
description: 
nav: true
nav_order: 6
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



<h4 style="text-align: left;">Presentations (e.g., Talks/Lectures)</h4>

<h5 style="text-align: left;">2025</h5>
<div class="talks-container">
  <ul class="talks-list invited-talks">
    <li>March 14, 2025: Li Auto Autonomous Driving Team, Virtual.<br>
    Topic: VLM-RL: Vision-Language Models for Reinforcement Learning in Autonomous Driving.</li>
  </ul>
</div>
