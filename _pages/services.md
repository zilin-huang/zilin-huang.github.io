---
layout: page
title: Services
permalink: /services/
description: 
nav: true
nav_order: 6
---

<style>
/* 基础样式 */
.services-container {
  margin-bottom: 20px;
}

.services-list {
  list-style-type: disc;
  padding-left: 1.5em;
}

.services-list li {
  position: relative;
  padding-left: 0.5em;
  margin-bottom: 0.3em;
  padding-bottom: 0.2em;
  border-bottom: none;
}

.services-list li:last-child {
  border-bottom: none;
}

/* 移除悬停效果 */
.services-list li:hover {
  background-color: transparent;
  padding-left: 0.5em;
  border-radius: 0;
}

/* 图标样式 */
.services-list li:before {
  content: none;
}

.academic-services li:before {
  content: none;
}

.community-services li:before {
  content: none;
}

.services-list li:hover:before {
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

/* 服务类型标签 */
.service-type {
  display: inline-block;
  font-size: 0.75em;
  padding: 2px 8px;
  margin-right: 8px;
  border-radius: 12px;
  vertical-align: middle;
}

.reviewer {
  background-color: rgba(33, 150, 243, 0.1);
  color: rgba(33, 150, 243, 0.8);
  border: 1px solid rgba(33, 150, 243, 0.2);
}

.member {
  background-color: rgba(76, 175, 80, 0.1);
  color: rgba(76, 175, 80, 0.8);
  border: 1px solid rgba(76, 175, 80, 0.2);
}

/* 响应式调整 */
@media (max-width: 768px) {
  .services-list li {
    padding-left: 2em;
    padding-bottom: 0.8em;
    margin-bottom: 0.8em;
  }
  
  .services-list li:hover {
    padding-left: 2.2em;
  }
}
</style>

<h4 style="text-align: left;">Academic Services</h4>

<div class="services-container">
  <h5 style="text-align: left;">Journal Reviewer</h5>
  <ul class="services-list academic-services">
    <li>IEEE Transactions on Intelligent Transportation Systems (TITS)</li>
    <li>IEEE Transactions on Intelligent Vehicles (TIV)</li>
    <li>Transportation Research Part C: Emerging Technologies (Part C)</li>
    <li>IEEE Transactions on Image Processing (TIP)</li>
    <li>IEEE Robotics and Automation Letters (RA-L)</li>
    <li>IEEE Intelligent Transportation Systems Magazine</li>
  </ul>
</div>

<div class="services-container">
  <h5 style="text-align: left;">Conference Reviewer</h5>
  <ul class="services-list academic-services">
    <li>Transportation Research Board Annual Meeting (TRB)</li>
    <li>IEEE Intelligent Vehicles Symposium (IV)</li>
    <li>IEEE Intelligent Transportation Systems Conference (ITSC)</li>
  </ul>
</div>

<div class="services-container">
  <h5 style="text-align: left;">Membership</h5>
  <ul class="services-list academic-services">
    <li>IEEE Student Member</li>
    <li>ASCE Student Member</li>
    <li>COTA Student Member</li>
  </ul>
</div>

<h4 style="text-align: left;">Community Services</h4>

<div class="services-container">
  <ul class="services-list community-services">
    <li>.</li>
  </ul>
</div> 