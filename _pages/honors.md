---
layout: page
title: Awards
permalink: /awards/
description: 
nav: true
nav_order: 7
---

<style>
/* 基础样式 */
.honors-container {
  margin-bottom: 20px;
}

.awards-list {
  list-style-type: disc;
  padding-left: 1.5em;
  margin-top: 0;
}

.awards-list li {
  position: relative;
  padding-left: 0.5em;
  margin-bottom: 0.5em;
  padding-bottom: 0.2em;
  border-bottom: none;
  line-height: 1.4;
}

.awards-list li:last-child {
  border-bottom: none;
}

/* 移除悬停效果 */
.awards-list li:hover {
  background-color: transparent;
  padding-left: 0.5em;
  border-radius: 0;
}

/* 移除图标样式 */
.awards-list li:before {
  content: none;
}

.academic-awards li:before {
  content: none;
}

.scholarships-list li:before {
  content: none;
}

.competitions-list li:before {
  content: none;
}

.awards-list li:hover:before {
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
  padding-left: 0;
  border-left: none;
}

/* 强调文本 */
.awards-list li strong {
  font-weight: 600;
  letter-spacing: 0.01em;
}

/* 描述文本样式 */
.award-description {
  display: inline-block;
  font-size: 1em;
  color: var(--global-text-color-light, #666);
  font-style: normal;
  margin-top: 0;
  line-height: 1.4;
}

/* 保留但优化br标签 */
.awards-list li br {
  display: block;
  content: "";
  margin: 0;
  line-height: 1;
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
  background-color: rgba(156, 39, 176, 0.1);
  color: rgba(156, 39, 176, 0.8);
  border: 1px solid rgba(156, 39, 176, 0.2);
}

/* 证书链接样式 */
.awards-list a {
  display: inline-block;
  transition: transform 0.2s;
}

.awards-list a:hover {
  transform: translateY(-1px);
}

/* 响应式调整 */
@media (max-width: 768px) {
  .awards-list li {
    padding-left: 2em;
    padding-bottom: 0.8em;
    margin-bottom: 1em;
  }
  
  h5 {
    font-size: 1.1em;
    padding-left: 8px;
    border-left: 3px solid rgba(var(--global-theme-color-rgb), 0.6);
  }
}
</style>

<h4 style="text-align: left;">Honors & Awards</h4>

<div class="honors-container">
  <h5 style="text-align: left;">2023</h5>
  <ul class="awards-list">
    <li><strong>Best Presentation Award, 3rd Annual Conference of Next-Generation Transportation Systems (NGTS-3), Wes Lafayette, USA </strong> <a href="{{ '2023-Best-Presentation-Award.pdf' | relative_url }}" target="_blank">[News Links]</a> </li>
    <li>Student Research Grants Competition (SRGC) Award, University of Wisconsin-Madison (USD $1,500)</li>
  </ul>
</div>

<div class="honors-container">
  <h5 style="text-align: left;">2021</h5>
  <ul class="awards-list">
    <li><strong>"Qinglan Plan" Competition Award, Guangzhou, China (RMB ¥50,000)</strong> <a href="{{ 'https://www.panyu.gov.cn/tgl/qkgsxj/content/post_6903583.html' | relative_url }}" target="_blank">[News Links]</a> <br>
    <span class="award-description">Awarded to students with high potential for commercial translation of their research.</span></li>
    <li><strong>Outstanding Master's Degree Graduates Award, Guangdong Province, China (≈ 1/340) </strong> <a href="{{ '/assets/honors/2021-outstanding-graduate-guangdong-province.jpg' | relative_url }}" target="_blank">[Certificate]</a>  <br>
    <span class="award-description">The highest graduate student honor, awarded to one graduate student with outstanding research potential and promise.</span></li>
  </ul>
</div>

<div class="honors-container">
  <h5 style="text-align: left;">2020</h5>
  <ul class="awards-list">
    <li><strong>Special Funds Project for Science and Technology Innovation Strateg Award, Guangdong Province, China (RMB ¥60,000) </strong><a href="{{ 'https://www.gdcyl.org/xxb/ShowArticle.asp?ArticleID=241940' | relative_url }}" target="_blank">[News Links]</a> <br>
    <span class="award-description">Awarded to students with very strong research potential (Key project, No. pdjh2020a0030).</span></li>
    <li><strong> "Win in Guangzhou" Competition Award, Guangzhou, China (RMB ¥50,000 + ¥100,000 startup fund)</strong> <a href="{{ 'https://www.gz.gov.cn/zwgk/zdly/jycy/gzdt/content/mpost_6999222.html' | relative_url }}" target="_blank">[News Links]</a> <br>
    <span class="award-description">Awarded to the young entrepreneur with promise of business success.</span></li>
    <li>National Scholarship for Graduate Student, China (RMB ¥20,000) <a href="{{ '/assets/honors/2020-national-scholarship.jpg' | relative_url }}" target="_blank">[Certificate]</a></li>
    <li>"Young Entrepreneur in Guangdong" Competition Award, Huizhou, China (RMB ¥30,000) <a href="{{ 'https://baijiahao.baidu.com/s?id=1672187346796437301&wfr=spider&for=pc' | relative_url }}" target="_blank">[News Links]</a> <br>
    <span class="award-description">Awarded to the young entrepreneur with promise of business success.</span></li>
  </ul>
</div>

<div class="honors-container">
  <h5 style="text-align: left;">2019</h5>
  <ul class="awards-list">
    <li>National Scholarship for Graduate Student, China (RMB ¥20,000) <a href="{{ '/assets/honors/2019-national-scholarship.jpg' | relative_url }}" target="_blank">[Certificate]</a></li>
    <li><strong>Graduate Student Academic Competition Award, SCUT (RMB ¥20,000)</strong><br>
    <span class="award-description">Awarded to students with very strong research potential (Key project, No. j2tw201904005).</span></li>
    <li>Science and Innovation Scholarships for Outstanding Graduate Students (RMB ¥2500 * 3) 
    <span class="award-description">Awarded for three consecutive years in 2019-2021 (three times).</span></li>
    <li>Top 100 PhD and Postdoctoral Innovation Achievements Award, Guangdong Province, China <a href="{{ '/assets/honors/2019-100-PhD-and-Postdoctoral-Innovation.pdf' | relative_url }}" target="_blank">[Certificate]</a> </li>
  </ul>
</div>

<div class="honors-container">
  <h5 style="text-align: left;">2018</h5>
  <ul class="awards-list">
    <li>Graduate Student Academic Competition Award, SCUT (RMB ¥5,000)<br>
    <span class="award-description">Awarded to students with strong research potential (No. j2tw202004010).</span></li>
    <li>2nd Prize Scholarship for Excellent Graduate Student (RMB ¥10,000 * 3)<br>
    <span class="award-description">Awarded for three consecutive years in 2018-2021 (three times).</span></li>
    <li>Outstanding Bachelor's Degree Graduates Award (≈ 10/780)</li>
    <li><strong>Top 10 Outstanding Undergraduate Students Award (≈ 10/40,000) </strong> <br>
    <span class="award-description">The highest undergraduate honor, awarded to the top 10 students with outstanding research potential and prospects.</span></li>
  </ul>
</div>

<div class="honors-container">
  <h5 style="text-align: left;">2017</h5>
  <ul class="awards-list">
    <li><strong>Special Funds Project for Science and Technology Innovation Strateg Award, Guangdong Province, China (RMB ¥20,000 + ¥10,000) </strong> <br>
    <span class="award-description">Awarded to students with strong research potential (No. phjh2017b0161 & No. phjh2017b0169).</span></li>
    <li>Top 10 Student Leader in Student Government Award (≈ 10/40,000)</li>
    <li>Outstanding Leader in Student Government Award, Guangdong Province, China (≈ 5/40,000)</li>
    <li>Science and Innovation Scholarships for Outstanding Undergraduate Students (Top 1%)</li>
    <li>Outstanding Volunteers Scholarship for Social Work (Top 1%)</li>
    <li>Outstanding Student Leadership Scholarship (Top 1%)</li>
  </ul>
</div>

<div class="honors-container">
  <h5 style="text-align: left;">2016</h5>
  <ul class="awards-list">
    <li>College Student 'Summer Rural Social Practice' Advanced Individual Award, Guangdong Province, China (≈ 6/40,000)</li>
    <li>Top 10 Student Volunteers for Social Work Award (≈ 10/40,000)</li>
  </ul>
</div>

<div class="honors-container">
  <h5 style="text-align: left;">2015</h5>
  <ul class="awards-list">
    <li>1st Prize Scholarship for Excellent Undergraduate Student (Top 2%, RMB ¥2500)<br>
    <span class="award-description">Awarded for three consecutive years in 2015-2017 (three times).</span></li>
  </ul>
</div>

<h4 style="text-align: left;">Academic Competitions Awards</h4>

<div class="honors-container">
  <h5 style="text-align: left;">2018</h5>
  <ul class="awards-list">
    <li><strong>The 15th China Graduate Student Mathematical Modeling Competition, China</strong> <a href="{{ '/assets/honors/2018-mathematical-modeling-competition.pdf' | relative_url }}" target="_blank">[Certificate]</a><br>
    National 1st Prize (Top 1.5%).<br>
    <span class="award-description">The competition selected 184 1st prizes from 12,207 projects in China.</span></li>
    <li><strong>The 2018 China College Student' Entrepreneurship Competition, China</strong> <a href="{{ '/assets/honors/2018-student-entrepreneurship-competition.jpg' | relative_url }}" target="_blank">[Certificate]</a><br>
    National 1st Prize (Top 0.08%).<br>
    <span class="award-description">The competition selected 124 1st prizes from more than 150,000 projects in China.</span></li>
  </ul>
</div>

<div class="honors-container">
  <h5 style="text-align: left;">2017</h5>
  <ul class="awards-list">
    <li><strong>The 15th "Challenge Cup" China College Student Academic Science and Technology Works Competition, China</strong> <a href="{{ '/assets/honors/2017-challenge-cup-competition.jpg' | relative_url }}" target="_blank">[Certificate]</a><br>
    National 2nd Prize (Top 0.06%).<br>
    <span class="award-description">The competition selected 315 2nd prizes from more than 600,000 projects in China.</span></li>
  </ul>
</div>

<div class="honors-container">
  <h5 style="text-align: left;">2016</h5>
  <ul class="awards-list">
    <li><strong>The 2nd China International College Students' "Internet+" Innovation and Entrepreneurship Competition, China</strong> <a href="{{ '/assets/honors/2016-internet-entrepreneurship-competition.pdf' | relative_url }}" target="_blank">[Certificate]</a><br>
    National 2nd Prize (Top 0.03%).<br>
    <span class="award-description">The competition selected 115 2nd prizes from more than 110,000 projects in China.</span></li>
    <li><strong>The 2016 China College Student' Entrepreneurship Competition, China</strong> <a href="{{ '/assets/honors/2016-student-entrepreneurship-competition.pdf' | relative_url }}" target="_blank">[Certificate]</a><br>
    National 2nd Prize (Top 0.03%).<br>
    <span class="award-description">The competition selected 262 2nd prizes from more than 120,000 projects in China.</span></li>
  </ul>
</div> 