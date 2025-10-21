---
layout: page
permalink: /research/
title: Research
description: 
nav: true
nav_order: 2
---

<style>
/* 专利相关样式 */
/* 基础列表样式 */
.artistic-list {
  counter-reset: item;
  list-style-type: none;
  padding-left: 0;
}

.artistic-list li {
  position: relative;
  padding-left: 2.4em;
  margin-bottom: 0.5em;
  padding-bottom: 0.4em;
  border-bottom: none;
}

.artistic-list li:last-child {
  border-bottom: none;
}

/* 数字标记样式 */
.artistic-list li:before {
  position: absolute;
  left: 0;
  top: -0.1em;
  counter-increment: item;
  content: counter(item);
  display: inline-block;
  font-weight: bold;
  font-size: 1.05em;
  width: 1.7em;
  height: 1.7em;
  line-height: 1.7em;
  border-radius: 50%;
  background-color: var(--global-card-bg-color);
  color: var(--global-theme-color);
  text-align: center;
  box-shadow: 0 2px 4px var(--global-shadow-color);
  border: 1px solid rgba(var(--global-theme-color-rgb), 0.2);
}

/* 链接样式 */
.artistic-list a {
  color: var(--global-theme-color);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  font-weight: 500;
}

.artistic-list a:after {
  content: "📄";
  margin-left: 5px;
  font-size: 0.9em;
}

/* 专利类型标签 */
.patent-type {
  display: inline-block;
  font-size: 0.75em;
  padding: 2px 8px;
  margin-right: 8px;
  border-radius: 12px;
  vertical-align: middle;
}

.invention {
  background-color: rgba(var(--global-theme-color-rgb), 0.1);
  color: var(--global-theme-color);
  border: 1px solid rgba(var(--global-theme-color-rgb), 0.2);
}

.utility-model {
  background-color: rgba(33, 150, 243, 0.1);
  color: rgba(33, 150, 243, 0.8);
  border: 1px solid rgba(33, 150, 243, 0.2);
}

.software {
  background-color: rgba(76, 175, 80, 0.1);
  color: rgba(76, 175, 80, 0.8);
  border: 1px solid rgba(76, 175, 80, 0.2);
}

/* 响应式调整 */
@media (max-width: 768px) {
  .artistic-list li {
    padding-left: 2em;
    padding-bottom: 1em;
    margin-bottom: 1em;
  }
  
  .artistic-list li:hover {
    padding-left: 2.2em;
  }
  
  .quote-section {
    margin: -90px 20px 40px 20px;
    padding: 20px;
  }
  
  .quote-text {
    font-size: 1em;
    line-height: 1.6;
  }
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
  transform: none;
  box-shadow: 0 2px 4px rgba(33, 150, 243, 0.05);
  background: linear-gradient(120deg, rgba(33, 150, 243, 0.12), rgba(3, 169, 244, 0.05));
}

/* 引用样式 */
.quote-section {
  position: relative;
  margin: -90px 40px 40px 40px;
  padding: 15px 40px;
  background: var(--global-bg-color);
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  text-align: center;
}

.quote-text {
  font-size: 1.06em;
  line-height: 1.8;
  color: var(--global-text-color);
  font-family: "Crimson Text", "Merriweather", "Lora", "Source Serif Pro", "Georgia", serif;
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
  font-size: 2.4em;
  font-weight: bold;
  text-align: center;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  padding: 20px;
  background-color: rgba(0, 0, 0, 0.3);
  border-radius: 8px;
}

/* 研究方向卡片样式 */
.research-area {
  padding: 0;
  margin-bottom: 25px;
  border-bottom: 1px dashed rgba(var(--global-theme-color-rgb), 0.1);
  padding-bottom: 20px;
}

.research-area:last-child {
  border-bottom: none;
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
  <div class="research-header-title"><u>H</u>uman-c<u>e</u>ntered <u>a</u>nd Trustwo<u>r</u>thy Au<u>t</u>onomous Systems (HEART)</div>
</div>

<!-- <h4>Research Vision</h4> -->

<div class="quote-section">
  <div class="quote-border"></div>
  <p class="quote-text">"HAL 9000 made the 'logical' choice—to kill the crew." This moment from 《2001: A Space Odyssey》 reveals a chilling truth: AI without alignment or trust can be dangerous. My research vision is to give technology a HEART: developing human-centered and trustworthy autonomous systems that truly understand, adapt to, and collaborate with humans. This is the key to building a future transportation systems where humans and AI-powered agents coexist in harmony.</p>
</div>


<h4>1. Simulation Platform Development</h4>

<div class="research-area">
  <h5>1.1 Multi-Agent Interaction</h5>
  <p>
    Developing an open-world simulation platform that supports unified simulation of diverse human and agents with realistic physical and social interactions. This platform enables comprehensive testing and validation of autonomous systems in complex, dynamic environments.
  </p>
  <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-top: 10px;">
    <div style="flex: 1; min-width: 300px;">
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/sky-drive-1.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Sky-Drive demo: distributed, multi-agent VR experiment.
      </p>
    </div>
    <div style="flex: 1; min-width: 300px;">
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/sky-drive-2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Sky-Drive overview.
      </p>
    </div>
  </div>
  <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 20px;">
    <div style="width: 24%;">
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/Right_Turn_Conflict -480p.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Safety-Critical Scenario: Right Turn Conflict.
      </p>
    </div>
    <div style="width: 24%;">
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/Nearside_Conflict_Straight_road-480p.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Safety-Critical Scenario: Nearside Conflict.
      </p>
    </div>
    <div style="width: 24%;">
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/Left_Turn_Conflict - 480p.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Safety-Critical Scenario: Left Turn Conflict.
      </p>
    </div>
    <div style="width: 24%;">
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/Farside_Conflict_Straight_road - 480p.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Safety-Critical Scenario: Farside Conflict.
      </p>
    </div>
  </div>
</div>

<h4>2. Human-centered AI Algorithm Design</h4>

<div class="research-area">
  <h5>2.1 Imitation Learning Pretraining</h5>
  <p>
    
  </p>
</div>

<div class="research-area">
  <h5>2.2 Closed-loop Post-Training: VLM, RL and WM</h5>
  <p>
    
  </p>
</div>

<div class="research-area">
  <h5>2.3 Human-in-the-loop Adaptation</h5>
  <p>
    
  </p>
</div>

<h4>3. Real-world Testing & Evaluation</h4>

<div class="research-area">
  <h5>3.1 Real-World Autonomous Driving Testbed</h5>
  <p>
     While simulation provides a safe and scalable environment for algorithm development, the sim-to-real gap remains a fundamental challenge. I am dedicated to transferring our developed human-centered AI algorithms to real-world environments to validate their effectiveness and robustness. Our primary platform is an electric Ford E-Transit van retrofitted with a complete autonomous driving stack: a drive-by-wire system, multi-modal sensor suite (e.g., 3 LiDARs, 7 cameras, and radars), 5G connectivity via NETGEAR Nighthawk M6 Pro, and high-performance onboard computing (RTX A6000). We have also deployed portable roadside units (Siemens RSUs, Cohda MK6C OBU) and traffic signals that can be configured to create customizable traffic scenarios at intersections and along corridors. This integrated Cyber-Physical Systems (CPS) testbed, combined with high-performance Lambda Servers that our team possesses, featuring multiple NVIDIA GPUs (RTX PRO 6000, A6000, 4090, and 4080), enables comprehensive testing of human-centered AI algorithms in real traffic conditions.
  </p>
  <div style="display: flex; gap: 5px; flex-wrap: wrap; margin-top: 20px; align-items: flex-start; justify-content: center;">
    <div>
      <img src="../assets/research/testbed/AV1.png" alt="Autonomous Vehicle Testbed 1" style="width: auto; height: 350px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" loading="lazy" decoding="async">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Autonomous Van with Sensor Suite
      </p>
    </div>
    <div>
      <img src="../assets/research/testbed/AV2.png" alt="Autonomous Vehicle Testbed 2" style="width: auto; height: 350px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" loading="lazy" decoding="async">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Driver Cockpit and Control Interface
      </p>
    </div>
    <div>
      <img src="../assets/research/testbed/AV3.png" alt="Autonomous Vehicle Testbed 3" style="width: auto; height: 350px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" loading="lazy" decoding="async">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Computing Hardware and Sensor Integration
      </p>
    </div>
      <div>
        <img src="../assets/research/testbed/AV4.jpg" alt="Autonomous Vehicle Testbed 4" style="width: auto; height: 350px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" loading="lazy" decoding="async">
        <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
          Portable Traffic Light
        </p>
      </div>
    </div>
    <div style="display: flex; gap: 5px; flex-wrap: wrap; margin-top: 20px; align-items: flex-start; justify-content: center;">
      <div>
        <img src="../assets/research/testbed/AV5.jpg" alt="Autonomous Vehicle Testbed 5" style="width: auto; height: 200px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" loading="lazy" decoding="async">
        <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
          Testbed
        </p>
      </div>
      <div>
        <img src="../assets/research/testbed/AV6.jpg" alt="Autonomous Vehicle Testbed 6" style="width: auto; height: 200px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" loading="lazy" decoding="async">
        <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
          Sensor Configuration
        </p>
      </div>
      <div>
        <img src="../assets/research/testbed/AV8.png" alt="Autonomous Vehicle Testbed 8" style="width: auto; height: 200px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" loading="lazy" decoding="async">
        <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
          V2X experiment equipment
        </p>
      </div>
      <div>
        <img src="../assets/research/testbed/AV7.png" alt="Autonomous Vehicle Testbed 7" style="width: auto; height: 200px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" loading="lazy" decoding="async">
        <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
          5G mmWave Mobile Hotspot
        </p>
      </div>
    </div>
</div>

<div class="research-area">
  <h5>3.3 Remote Vehicle Operations and Cloud-Based AI Deployment</h5>
  <p>
    Deploying VLMs and complex AI algorithms directly on vehicle computer hardware faces significant computational constraints. To address this limitation, my team and I designed a complete remote operations (teleoperation) platform for our autonomous van. Leveraging its 5G connectivity, the vehicle can be controlled in real time for driving, operation, and data collection from any location with an internet connection, such as a conference room or an off-site lab (see video examples below). More importantly, our platform is designed for remote AI model deployment. This enables a powerful hardware-in-the-loop workflow: real-time sensor data is streamed from the vehicle to a local computer or a cloud service like Amazon Web Services (AWS), where AI models can process the data and transmit control commands back to the vehicle for immediate execution.
  </p>
  <div style="display: flex; gap: 20px; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 300px;">
      <video width="100%" controls>
        <source src="../assets/research/remote control/sky-remote-driving-1min.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Prof. Chen remote driving from the office. The van can be seen passing the window on the right at 0:02 and 0:42.
      </p>
    </div>
    <div style="flex: 1; min-width: 300px;">
      <video width="100%" controls>
        <source src="../assets/research/remote control/remote control - 4speed - 480p.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        My team and I testing remote driving function with Logitech G920 Racing Wheel and Pedals. Full video on <a href="https://www.youtube.com/embed/Lj6kqDByaEI?si=c1Jzdf6PukLNb1c4" target="_blank">YouTube</a>.
      </p>
    </div>
  </div>
</div>


<!-- <h4>Team Facilities</h4> -->