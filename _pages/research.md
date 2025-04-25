---
layout: page
permalink: /projects/
title: Research
description: 
nav: true
nav_order: 2
---

<style>
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

/* 背景图片样式 */
.research-header {
  width: 100%;
  height: 250px;
  background-image: url('../../assets/research/av_background.jpg');
  background-size: cover;
  background-position: center 80%;
  margin-bottom: 30px;
  border-radius: 5px;
  margin-top: -20px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 添加标题文字样式 */
.research-header-title {
  color: white;
  font-size: 2.5em;
  font-weight: bold;
  text-align: center;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  padding: 20px;
  background-color: rgba(0, 0, 0, 0.3);
  border-radius: 8px;
}

/* 研究方向卡片样式 */
.research-area {
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 25px;
  box-shadow: 0 3px 10px rgba(0,0,0,0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.research-area:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.research-area h5 {
  color: var(--global-theme-color);
  font-weight: 600;
  margin-bottom: 15px;
  font-size: 1.1em;
}

.research-area p {
  margin-bottom: 12px;
  text-align: justify;
}
</style>

<div class="research-header">
  <div class="research-header-title">Human-centered AI & Transportation</div>
</div>

<h4>Research Vision</h4>

<!-- <p>
My research vision is to develop next-generation intelligent transportation systems through the integration of artificial intelligence, robotics, and human-centered design. My work bridges fundamental theoretical research with practical applications, creating solutions that enhance transportation safety, efficiency, and sustainability.
</p>

<p>
The ultimate goal of my research is to develop <b>Human-centered</b>, <b>Trustworthy</b>, and <b>Interactive</b> autonomous embodied agents that can perceive, understand, and reason about complex transportation environments; safely interact and collaborate with road users; and efficiently coordinate with other intelligent agents so that they can benefit society in daily life by enhancing travel <b>Safety</b>, <b>Mobility</b>, <b>Efficiency</b>, and <b>Sustainability</b>.
</p> -->
<!-- 
<h4>Research Areas</h4>

<div class="research-area">
  <h5>Human-AI Collaborative Systems</h5>
  <p>
    Developing frameworks for effective cooperation between humans and autonomous agents in transportation contexts. My research explores how to design AI systems that can understand human intentions, adapt to human preferences, and collaborate efficiently with human operators or passengers. This includes investigating natural interaction methodologies, shared control mechanisms, and intuitive interfaces to facilitate human-AI partnerships in transportation.
  </p>
</div>

<div class="research-area">
  <h5>Multi-Agent Reinforcement Learning</h5>
  <p>
    Creating cooperative behaviors for autonomous vehicles in complex traffic scenarios. My work in this area focuses on developing algorithms that enable multiple autonomous vehicles to coordinate their actions effectively in dynamic traffic environments. This research addresses challenges in distributed decision-making, coordination under uncertainty, and balancing individual and collective objectives in traffic management.
  </p>
</div>

<div class="research-area">
  <h5>Trustworthy AI for Transportation</h5>
  <p>
    Building robust, explainable, and fair AI systems for critical transportation applications. This research direction explores how to develop AI systems that are reliable in diverse and unpredictable situations, capable of explaining their decisions to users, and designed to treat all road users equitably. My work addresses challenges in robustness against distribution shifts, interpretable decision-making models, and fairness considerations in autonomous systems.
  </p>
</div>

<div class="research-area">
  <h5>Foundation Models for Autonomous Driving</h5>
  <p>
    Leveraging large language and vision models to enhance environmental perception and decision-making. My research investigates how to adapt and fine-tune foundation models to improve autonomous vehicles' ability to understand complex road scenarios, interpret traffic rules and social norms, and reason about multi-agent interactions. This includes developing multimodal approaches that combine visual perception with semantic understanding of traffic environments.
  </p>
</div>

<div class="research-area">
  <h5>Cognitive Systems for Mobility</h5>
  <p>
    Designing intelligent agents with human-like reasoning capabilities for navigation in dynamic environments. This research direction explores cognitive architectures that enable autonomous systems to reason about traffic situations, make decisions under uncertainty, and adapt to novel environments. My work aims to develop agents that can understand the implicit rules of the road and navigate complex social interactions in shared spaces.
  </p>
</div> -->
<!-- 
<h4>Research Impact</h4>

<p>My research contributions are documented in peer-reviewed publications spanning transportation science, artificial intelligence, and robotics. My work has addressed key challenges in:</p>

<ul>
  <li>Developing robust control strategies for mixed-autonomy traffic systems</li>
  <li>Creating trustworthy AI systems for safety-critical transportation applications</li>
  <li>Designing adaptive human-AI interfaces for autonomous vehicle interaction</li>
  <li>Applying foundation models to enhance environmental perception in complex driving scenarios</li>
</ul> -->


<!-- <h4>Selected Projects</h4>

<div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; display: flex;">
  <img src="../../assets/img/projects_photo/frank-GCQ.gif" style="width: 300px; height: 250px; margin-right: 20px;">
  <div>
    <h5><strong><span style="color: #B71C1C;">Graph neural network and reinforcement learning for multi-agent cooperative control of connected autonomous vehicles</span></strong></h5>
    <h6>Publication</h6>
    <ul>
      <li>Computer‐Aided Civil and Infrastructure Engineering, 2021, 36(7): 838-857.</li>
    </ul>
  </div>
</div>

<br>

<div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; display: flex;">
  <img src="../../assets/img/projects_photo/Paul-research.gif" style="width: 300px; height: 250px; margin-right: 20px;">
  <div>
    <h5><strong><span style="color: #B71C1C;">Leveraging the capabilities of connected and autonomous vehicles and multi-agent reinforcement learning to mitigate highway bottleneck congestion</span></strong></h5>
    <h6>Publication</h6>
    <ul>
      <li>Transportmetrica A: Transportation Science</li>
    </ul>
  </div>
</div>

<br>

<div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; display: flex;">
  <img src="../../assets/img/projects_photo/crash_avoidance.gif" style="width: 300px; height: 250px; margin-right: 20px;">
  <div>
    <h5><strong><span style="color: #B71C1C;">A cooperative crash avoidance framework for autonomous vehicle under collision-imminent situations in mixed traffic stream</span></strong></h5>
    <h6>Publication</h6>
    <ul>
      <li>2021 IEEE International Intelligent Transportation Systems Conference (ITSC). IEEE, 2021: 1997-2002.</li>
    </ul>
  </div>
</div>


 -->


<h4>Selected Projects</h4>