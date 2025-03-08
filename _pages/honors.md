---
layout: page
title: Honors
permalink: /honors/
description: 
nav: true
nav_order: 6
---

<style>
/* 基础列表样式 */
.awards-list {
  list-style-type: none;
  padding-left: 0;
}

.awards-list li {
  position: relative;
  padding-left: 2.5em;
  margin-bottom: 1.2em;
  padding-bottom: 0.8em;
  border-bottom: 1px dashed rgba(var(--global-theme-color-rgb), 0.1);
  transition: all 0.3s ease;
}

.awards-list li:last-child {
  border-bottom: none;
}

.awards-list li:hover {
  background-color: rgba(var(--global-theme-color-rgb), 0.03);
  padding-left: 3em;
  border-radius: 4px;
}

/* 图标样式 */
.awards-list li:before {
  position: absolute;
  left: 0;
  top: 0;
  content: "🏆";
  font-size: 1.3em;
  transition: transform 0.3s ease;
}

/* 为不同部分设置特殊图标 */
.academic-awards li:before {
  content: "🏆";
  font-size: 1.3em;
}

.scholarships-list li:before {
  content: "🌟";
  font-size: 1.3em;
}

.competitions-list li:before {
  content: "🏅";
  font-size: 1.3em;
}

.awards-list li:hover:before {
  transform: scale(1.2);
}

/* 年份标签样式 */
.award-year {
  display: inline-block;
  font-size: 0.85em;
  padding: 2px 8px;
  margin-right: 8px;
  border-radius: 12px;
  font-weight: 500;
  vertical-align: middle;
}

/* 为不同部分的年份标签设置不同颜色 */
.academic-awards .award-year {
  background-color: rgba(156, 39, 176, 0.1);
  color: rgba(156, 39, 176, 0.8);
  border: 1px solid rgba(156, 39, 176, 0.2);
}

.scholarships-list .award-year {
  background-color: rgba(33, 150, 243, 0.1);
  color: rgba(33, 150, 243, 0.8);
  border: 1px solid rgba(33, 150, 243, 0.2);
}

.competitions-list .award-year {
  background-color: rgba(76, 175, 80, 0.1);
  color: rgba(76, 175, 80, 0.8);
  border: 1px solid rgba(76, 175, 80, 0.2);
}

/* 奖项类型标签 */
.award-type {
  display: inline-block;
  font-size: 0.75em;
  padding: 2px 8px;
  margin-right: 8px;
  border-radius: 12px;
  vertical-align: middle;
}

.scholarship {
  background-color: rgba(33, 150, 243, 0.1);
  color: rgba(33, 150, 243, 0.8);
  border: 1px solid rgba(33, 150, 243, 0.2);
}

.competition {
  background-color: rgba(76, 175, 80, 0.1);
  color: rgba(76, 175, 80, 0.8);
  border: 1px solid rgba(76, 175, 80, 0.2);
}

.academic {
  background-color: rgba(156, 39, 176, 0.1);
  color: rgba(156, 39, 176, 0.8);
  border: 1px solid rgba(156, 39, 176, 0.2);
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

/* 响应式调整 */
@media (max-width: 768px) {
  .awards-list li {
    padding-left: 2em;
    padding-bottom: 1em;
    margin-bottom: 1em;
  }
  
  .awards-list li:hover {
    padding-left: 2.2em;
  }
}
</style>


<h4 style="text-align: left;">Scholarships</h4>
<ul class="awards-list scholarships-list">
  <li>
    <span class="award-year">2020</span>
    <strong>National Scholarship for Graduate Student, China (RMB ¥20,000)</strong> 
  </li>
  <li>
    <span class="award-year">2018-2020</span>
    <strong>Science and Innovation Scholarships for Outstanding Graduate Students</strong><br>
    Awarded for three consecutive years in 2018-2020 (three times).
  </li>
  <li>
    <span class="award-year">2019</span>
    <strong>National Scholarship for Graduate Student, China (RMB ¥20,000)</strong> 
  </li>
  <li>
    <span class="award-year">2015-2017</span>
    <strong>1st Prize Scholarship for Excellent Student (Top 2%)</strong><br>
     Awarded for three consecutive years in 2015-2017 (three times).
  </li>
  <li>
    <span class="award-year">2017</span>
    <strong>Science and Innovation Scholarships for Outstanding Undergraduate Students </strong>
  </li>
  <li>
    <span class="award-year">2017</span>
    <strong>Outstanding Volunteers Scholarship for Community Service (Top 1%)</strong>
  </li>
  <li>
    <span class="award-year">2017</span>
    <strong>Outstanding Student Leadership Scholarship (Top 1%)</strong>
  </li>
</ul>

<h4 style="text-align: left;">Honors</h4>
<ul class="awards-list academic-awards">
  <li>
    <span class="award-year">2021</span>
    <strong>Outstanding Master's Degree Graduates, Guangdong Province (≈ 1/340)</strong> 
    <a href="{{ '/assets/honors/2021-outstanding_graduate_guangdong_province.jpg' | relative_url }}" target="_blank">[Certificate]</a><br>
    The highest graduate student honor, awarded to one graduate student with outstanding research potential and promise.
  </li>
  <li>
    <span class="award-year">2018</span>
    <strong>Outstanding Bachelor's Degree Graduates (≈ 10/780)</strong>
  </li>
  <li>
    <span class="award-year">2017</span>
    <strong>Top 10 Outstanding College Students (≈ 10/40,000)</strong><br>
    The highest undergraduate honor, awarded to the top 10 students with outstanding research potential and prospects.<br>
  </li>
  <li>
    <span class="award-year">2017</span>
    <strong>Top 10 Student Leader in Student Government (≈ 10/40,000)</strong>
  </li>
  <li>
    <span class="award-year">2017</span>
    <strong>Outstanding Leader in Student Government, Guangdong Province (≈ 5/40,000)</strong>
  </li>
  <li>
    <span class="award-year">2016</span>
    <strong>Top 10 Student Volunteers for Community Service (≈ 10/40,000)</strong>
  </li>
  <li>
    <span class="award-year">2016</span>
    <strong>College Student 'Summer Rural Social Practice' Advanced Individual Award, Guangdong Province (≈ 6/40,000)</strong>
  </li>
</ul>

<h4 style="text-align: left;">Academic Competitions Awards</h4>
<ul class="awards-list competitions-list">
  <li>
    <span class="award-year">2018</span>
    <strong>The 15th China Graduate Student Mathematical Modeling Competition</strong> 
    <a href="{{ '/assets/honors/2018-mathematical-modeling-competition.pdf' | relative_url }}" target="_blank">[Certificate]</a><br>
    National 1st Prize (Top 1.5%).<br>
    The competition selected 184 1st prizes from 12,207 projects in China.
  </li>
  <li>
    <span class="award-year">2018</span>
    <strong>The 2018 China College Student' Entrepreneurship Competition</strong>
    <a href="{{ '/assets/honors/2018-student-entrepreneurship-competition.jpg' | relative_url }}" target="_blank">[Certificate]</a><br>
    National 1st Prize (Top 0.08%).<br>
    The competition selected 124 1st prizes from more than 150,000 projects in China.
  </li>
  <li>
    <span class="award-year">2017</span>
    <strong>The 15th "Challenge Cup" China College Student Academic Science and Technology Works Competition</strong>    
    <a href="{{ '/assets/honors/2017-challenge-cup-competition.jpg' | relative_url }}" target="_blank">[Certificate]</a><br>
    National 2nd Prize (Top 0.06%).<br>
    The competition selected 315 2nd prizes from more than 600,000 projects in China.
  </li>
  <li>
    <span class="award-year">2016</span>
    <strong>The 2nd China International College Students' "Internet+" Innovation and Entrepreneurship Competition</strong>
    <a href="{{ '/assets/honors/2016-internet-entrepreneurship-competition.pdf' | relative_url }}" target="_blank">[Certificate]</a><br>
    National 2nd Prize (Top 0.03%).<br>
    The competition selected 115 2nd prizes from more than 110,000 projects in China.
  </li>
  <li>
    <span class="award-year">2016</span>
    <strong>The 2016 China College Student' Entrepreneurship Competition</strong>
    <a href="{{ '/assets/honors/2016-student-entrepreneurship-competition.pdf' | relative_url }}" target="_blank">[Certificate]</a><br>
    National 2nd Prize (Top 0.03%).<br>
    The competition selected 262 2nd prizes from more than 120,000 projects in China.
  </li>
</ul> 