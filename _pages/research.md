---
layout: page
permalink: /research/
title: Research
description: "Research vision, themes, platforms, and future directions in human-centered and trustworthy autonomous systems."
nav: true
nav_order: 2
wide_content: true
---

<style>
/* 专利相关样式 */
/* 基础列表样式 */
.artistic-list {
  counter-reset: item;
  list-style-type: none;
  padding-left: 0;
  margin-bottom: 0;
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
  margin-bottom: 0;
  padding-bottom: 0;
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

  .testbed-grid {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}

/* 标题样式 */
h4 {
  position: relative;
  padding-bottom: 10px;
  margin-bottom: 12px;
  margin-top: 30px;
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
  margin-top: 0;
  margin-bottom: 8px;
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
  background-image: url('../../assets/research/vision_background.png');
  background-size: cover;
  background-position: center 80%;
  margin-bottom: 30px;
  border-radius: 5px;
  margin-top: 0;
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
  margin-bottom: 14px;
  border-bottom: 1px dashed rgba(var(--global-theme-color-rgb), 0.1);
  padding-bottom: 10px;
}

.research-area:last-child {
  border-bottom: none;
}

.research-area h5 {
  color: var(--global-text-color);
  font-weight: 600;
  margin-bottom: 8px;
  font-size: 1.1em;
}

.research-area p {
  margin-bottom: 12px;
  text-align: justify;
}

.research-area img + p {
  margin: 8px 0 0 !important;
}

.research-area + h4 {
  margin-top: 16px;
}

.theme-question {
  font-weight: 600;
}

.theme-number {
  color: var(--global-theme-color);
  margin-right: 0.25em;
}

.featured-work-heading {
  margin: 16px 0 10px;
  padding-left: 12px;
  border-left: 3px solid var(--global-theme-color);
}

.featured-work-label {
  display: block;
  margin-bottom: 2px;
  color: var(--global-text-color-light);
  font-size: 0.72em;
  font-weight: 600;
  letter-spacing: 0.09em;
  line-height: 1.3;
  text-transform: uppercase;
}

.featured-work-title {
  margin: 0;
  color: var(--global-text-color);
  font-size: 1.08em;
  font-weight: 600;
  line-height: 1.35;
}

.featured-work-heading--list .project-links {
  margin-top: 8px;
}

.research-demo {
  max-width: 760px;
  margin: 18px auto 0;
}

.scenario-video-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px;
  margin-top: 14px;
}

.project-links {
  display: flex;
  flex-wrap: wrap;
  column-gap: 18px;
  row-gap: 5px;
  margin-top: 14px;
}

.project-links a,
.project-links span {
  display: inline-block;
  padding: 0;
  border: 0;
  border-radius: 0;
  background: none;
}

.platform-subsection {
  margin-top: 18px;
  padding-top: 14px;
  border-top: 1px dashed rgba(var(--global-theme-color-rgb), 0.15);
}

.platform-subsection h6 {
  color: var(--global-text-color);
  font-size: 1.05em;
  font-weight: 600;
  margin-bottom: 12px;
}

.platform-gallery {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
  margin-top: 18px;
}

.platform-gallery.two-column {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.platform-gallery figure,
.platform-gallery > div {
  margin: 0;
  text-align: center;
}

.platform-gallery img,
.platform-gallery > div img {
  width: 100%;
  height: 220px;
  object-fit: cover;
}

.platform-gallery figcaption {
  margin-top: 8px;
  color: var(--global-text-color-light);
  font-size: 0.85em;
}

.past-research-intro {
  margin-bottom: 16px;
}

.past-research-grid {
  display: block;
}

.past-research-group {
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px dashed rgba(var(--global-theme-color-rgb), 0.12);
}

.past-research-group:last-child {
  margin-bottom: 0;
}

.past-research-period {
  margin: -2px 0 8px;
  color: var(--global-text-color-light);
  font-size: 0.9em;
  font-style: italic;
}

.past-research-group ul {
  margin: 0;
  padding-left: 1.25em;
}

.past-research-group li {
  margin-bottom: 8px;
}

.related-publications {
  margin-top: 14px;
}

.related-publications-label {
  margin: 0 0 5px;
  color: var(--global-text-color);
  font-size: 0.95em;
  font-weight: 600;
}

.past-research-group .related-publications-list {
  margin: 0;
  padding-left: 1.4em;
  list-style: decimal;
  color: var(--global-text-color-light);
  font-size: 0.88em;
  line-height: 1.45;
}

.past-research-group .related-publications-list li {
  margin-bottom: 4px;
  padding-left: 0;
}

.earlier-media-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
  margin-top: 16px;
}

.earlier-media-card {
  margin: 0;
  text-align: center;
}

.earlier-media-frame {
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  border-radius: 6px;
  background: #000;
  box-shadow: 0 2px 7px var(--global-shadow-color);
}

.earlier-media-frame iframe,
.earlier-media-frame img {
  display: block;
  width: 100%;
  height: 100%;
  border: 0;
  object-fit: cover;
}

.earlier-media-frame--diagram {
  padding: 10px;
  background: #fff;
}

.earlier-media-frame--diagram img {
  object-fit: contain;
}

.earlier-media-card figcaption {
  margin-top: 8px;
  color: var(--global-text-color-light);
  font-size: 0.85em;
}

.research-prose {
  max-width: 100%;
  margin-left: auto;
  margin-right: auto;
}

.vision-section::after {
  content: "";
  display: table;
  clear: both;
}

.research-framework {
  float: right;
  width: 60%;
  max-width: 760px;
  margin: 0 0 18px 28px;
  text-align: center;
}

.research-framework img {
  width: 100%;
  display: block;
}

@media (max-width: 768px) {
  .research-framework {
    float: none;
    width: 100%;
    max-width: none;
    margin: 0 0 18px;
  }

  .platform-gallery,
  .platform-gallery.two-column,
  .past-research-grid,
  .earlier-media-grid {
    grid-template-columns: 1fr;
  }

  .scenario-video-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .featured-work-heading {
    padding-left: 10px;
  }

  .platform-gallery img {
    height: auto;
    aspect-ratio: 4 / 3;
  }
}

@media (min-width: 1200px) {
  body.wide-content-page > .container.mt-5 {
    max-width: 1280px;
  }
}
</style>

<div class="research-header">
  <div class="research-header-title"><u>H</u>uman-c<u>e</u>ntered <u>a</u>nd Trustwo<u>r</u>thy Au<u>t</u>onomous Systems (HEART)</div>
</div>

<div class="research-prose vision-section">
<h4>Research Vision</h4>

<div class="research-framework">
  <img src="../../assets/research/visionfull.jpg" alt="Research framework for Human-centered and Trustworthy Autonomous Systems" style="border-radius: 8px;"/>
</div>

<p>
  My research interests lie at the intersection of <strong>Physical AI</strong> and <strong>human-centered transportation systems</strong>. I envision future mobility as a <strong>human–robot–society ecosystem</strong>, where humans coexist, interact, and collaborate with diverse autonomous agents, including self-driving vehicles, delivery robots, drones, and other embodied systems. To thrive in such environments, these agents must understand complex physical and social contexts, reason about their actions, adapt to human preferences and social norms, and operate safely and reliably under open-world uncertainty.
</p>

<p>
  My long-term goal is to develop <strong>Human-centered and Trustworthy Autonomous Systems (HEART)</strong> that can safely learn, interact, and collaborate with people in the physical world.
</p>
</div>

<div class="research-prose">
<h4>Research Themes</h4>

<div class="research-area theme-block">
  <h5><span class="theme-number">1.</span> Human-Aware Intelligence and Decision-Making</h5>
  <p class="theme-question">How can autonomous agents understand complex physical and social environments and make safe, reliable, and human-aware decisions?</p>
  <p>I integrate human-guided reinforcement learning, physics-informed feedback, and foundation-model-based semantic reasoning to improve safe decision-making.</p>
  <div class="featured-work-heading featured-work-heading--list">
    <span class="featured-work-label">Featured Work</span>
    <div class="project-links">
      <a href="https://zilin-huang.github.io/HAIM-DRL-website/" target="_blank">HAIM-DRL</a>
      <a href="https://www.huang-zilin.com/PE-RLHF-website/" target="_blank">PE-RLHF</a>
      <a href="https://www.huang-zilin.com/VLM-RL-website/" target="_blank">VLM-RL</a>
      <a href="https://arxiv.org/abs/2603.18315" target="_blank">DriveVLM-RL</a>
      <a href="https://arxiv.org/abs/2602.10458" target="_blank">Found-RL</a>
    </div>
  </div>
</div>

<div class="research-area theme-block">
  <h5><span class="theme-number">2.</span> Generalization, Adaptation, and Real-World Deployment</h5>
  <p class="theme-question">How can capabilities learned in simulation or encoded in foundation models generalize, adapt, and transfer to real physical systems?</p>
  <p>I investigate deployment gaps, model selection, data-efficient adaptation, and evaluation across environments, embodiments, sensing configurations, and physical platforms.</p>
  <div class="featured-work-heading featured-work-heading--list">
    <span class="featured-work-label">Featured Work</span>
    <div class="project-links">
      <a href="https://arxiv.org/abs/2604.03497" target="_blank">Sim2Real-AD</a>
      <span>TRIAGE</span>
      <span>DOSE</span>
      <span>ExecGap</span>
      <span>MadisonTwin</span>
    </div>
  </div>
</div>

<div class="research-area theme-block">
  <h5><span class="theme-number">3.</span> Safe Continuous Improvement and Evaluation</h5>
  <p class="theme-question">How can autonomous agents safely and continuously improve through physical interaction, failure discovery, and real-world feedback?</p>
  <p>I explore closed-loop testing, independent evaluation designed to resist reward hacking, and verifiable policy improvement under limited real-world testing budgets.</p>
  <div class="featured-work-heading">
    <span class="featured-work-label">Featured Work</span>
    <h6 class="featured-work-title">Sky-Drive Simulation Platform</h6>
  </div>
  <p>
    Existing simulators often optimize traffic flow or validate a single vehicle, but lack distributed, multi-agent support. To address this gap, my colleagues and I at Sky-Lab developed Sky-Drive—a long-term effort with many contributors; I have been involved since Summer 2023. Sky-Drive integrates Unreal Engine/CARLA, ROS, WebSocket, and custom scenario pipelines to run synchronized simulations across multiple terminals. Unlike single-vehicle or flow-only tools, Sky-Drive emphasizes synchronized interactions among pedestrians, human-driven vehicles (HVs), and autonomous vehicles (AVs), and supports multi-participant intervention and co-study for human-AI collaborative driving research.
  </p>
  <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-top: 18px;">
    <div style="flex: 1; min-width: 300px;">
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/sky-drive-2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Sky-Drive overview.
      </p>
    </div>
    <div style="flex: 1; min-width: 300px;">
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/sky-drive-1.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        My colleagues and I at Sky-Lab are conducting the multi-agent VR experiment.
      </p>
    </div>
  </div>
  <div class="scenario-video-grid">
    <div>
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/Right_Turn_Conflict -480p.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">Safety-Critical Scenario: Right Turn Conflict.</p>
    </div>
    <div>
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/Nearside_Conflict_Straight_road-480p.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">Safety-Critical Scenario: Nearside Conflict.</p>
    </div>
    <div>
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/Left_Turn_Conflict - 480p.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">Safety-Critical Scenario: Left Turn Conflict.</p>
    </div>
    <div>
      <video width="100%" controls>
        <source src="../assets/research/mutli-agent interaction/Farside_Conflict_Straight_road - 480p.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">Safety-Critical Scenario: Farside Conflict.</p>
    </div>
  </div>
</div>
</div>

<h4>Research Platforms</h4>

<div class="research-area">
  <h5>Autonomous Vehicle Testbed</h5>
  <p>
    While simulation is safe and scalable, the sim-to-real gap remains a core challenge. At Sky-Lab, we maintain a real-world testbed that I actively use with my colleagues to validate human-centered AI algorithms. Our primary platform is a retrofit electric Ford E-Transit with a full autonomy stack: drive-by-wire, a multi-modal sensor suite (3 LiDARs, 7 cameras, radar), 5G connectivity (NETGEAR Nighthawk M6 Pro), and on-board GPU computing (RTX A6000). We also deploy portable RSUs/OBUs (e.g., Siemens RSUs, Cohda MK6C) and configurable traffic signals to create intersection and corridor scenarios. Combined with Sky-Lab’s Lambda servers (RTX Pro 6000, A6000, 4090, 4080), this cyber-physical setup lets me run end-to-end evaluations, collect edge cases, and iterate quickly on model design and safety checks in real traffic conditions.
  </p>
  <div class="platform-gallery">
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV1.png" alt="Autonomous Vehicle Testbed 1" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Autonomous Van with Sensor Suite
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV3.png" alt="Autonomous Vehicle Testbed 2" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Driver Cockpit and Control Interface
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV2.png" alt="Autonomous Vehicle Testbed 3" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Computing Hardware
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV4.jpg" alt="Autonomous Vehicle Testbed 4" style="object-position: top;" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Portable Traffic Light
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV5.jpg" srcset="../assets/research/testbed/AV5-thumb-900.webp 900w, ../assets/research/testbed/AV5-thumb-1600.webp 1600w" sizes="(max-width: 768px) 100vw, 25vw" alt="Autonomous Vehicle Testbed 5" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Testbed
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV6.jpg" alt="Autonomous Vehicle Testbed 6" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Sensor Configuration
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV8.png" alt="Autonomous Vehicle Testbed 8" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        V2X Experiment Equipment
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV7.png" alt="Autonomous Vehicle Testbed 7" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        5G mmWave Mobile Hotspot
      </p>
    </div>
  </div>

  <div class="platform-subsection">
    <h5>End-to-End Autonomous Driving</h5>
    <p>
      To evaluate designed end-to-end (E2E) driving policies in the real world, my colleagues and I at Sky-Lab deploy them on our lab-developed autonomous van for systematic testing and iterative refinement. Real-time streams from the multimodal perception suite (LiDAR, cameras, radar) feed the E2E policy, which outputs steering, throttle, and brake commands at ~20 Hz for closed-loop control. Through testing on public roads and our campus testbed, we continuously log performance and edge cases to inform model improvements.
    </p>
    <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-top: 10px;">
      <div style="flex: 1; min-width: 300px;">
        <video width="100%" controls>
          <source src="../assets/research/E2E/end-to-end-2.mp4" type="video/mp4">
          Your browser does not support the video tag.
        </video>
        <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
          End-to-end autonomous driving in urban and rural environments (McKee Road, Madison).
        </p>
      </div>
      <div style="flex: 1; min-width: 300px;">
        <video width="100%" controls>
          <source src="../assets/research/E2E/end-to-end-1.mp4" type="video/mp4">
          Your browser does not support the video tag.
        </video>
        <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
          Live demo at the 2025 AAA Safe Mobility Conference, Madison, WI.
        </p>
      </div>
    </div>
  </div>

</div>

<div class="research-area">
  <h5>Remote Operation and Cloud Deployment</h5>
  <p>
    Deploying large VLMs and complex AI stacks directly on vehicle hardware is often compute-limited. To overcome this, my colleagues and I at Sky-Lab built a remote operations (teleoperation) and remote-inference platform for our autonomous van. Using 5G connectivity, we can remotely operate the vehicle for driving and data collection from locations such as a conference room or off-site lab. The platform also supports remote AI deployment: real-time sensor streams are sent from the van to a local workstation or cloud (e.g., AWS), where models process the data and return control commands to the vehicle for execution.
  </p>
  <div style="display: flex; gap: 20px; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 300px;">
      <video width="100%" controls>
        <source src="../assets/research/remote control/remote control - 4speed - 480p.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        My colleagues and I testing remote driving function with Logitech G920 Racing Wheel and Pedals. Full video on <a href="https://www.youtube.com/embed/Lj6kqDByaEI?si=c1Jzdf6PukLNb1c4" target="_blank">YouTube</a>.
      </p>
    </div>
    <div style="flex: 1; min-width: 300px;">
      <video width="100%" controls>
        <source src="../assets/research/remote control/sky-remote-driving-1min.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Prof. Chen remote driving from the office. 
      </p>
    </div>
  </div>
</div>

<div class="research-prose">
<h4>Earlier Research Foundations</h4>

<p class="past-research-intro">
  My earlier research established foundations in wireless sensing, transportation data mining, vehicle localization and control, and digital-twin optimization. These projects continue to inform my current work on human-centered and trustworthy autonomous systems.
</p>

<div class="past-research-grid">
  <div class="past-research-group">
    <h5>Autonomous Driving, Localization, and Mobility Recognition</h5>
    <p class="past-research-period">2018–2021</p>
    <ul>
      <li><strong>Autonomous Vehicle Path Tracking and Visual Localization</strong>: I evaluated model predictive control and conventional pure-pursuit tracking through practical vehicle experiments. I also explored DBow3-based visual place recognition to support camera-assisted localization.</li>
      <li><strong>RSSI-Based Location Awareness and Travel-Mode Recognition</strong>: My Master’s thesis developed fingerprint- and ranging-based methods for accurate, fast, and robust localization across different spatial scales. It also introduced a travel-mode classification method using single-point wireless sensing data.</li>
      <li><strong>Robust Outdoor Pedestrian Positioning with WiFi RSSI</strong>: I developed a multi-stage outdoor positioning framework that combines probabilistic RSSI modeling, filtering, and location estimation. The framework was designed to remain robust under substantial real-time RSSI fluctuations.</li>
      <li><strong>GPS-Denied Vehicle Localization in Tunnels</strong>: I combined semi-supervised extreme learning with locally linear embedding to learn from both labeled and unlabeled RSSI samples. The resulting method estimates vehicle positions in GPS-denied tunnel and parking environments.</li>
    </ul>
    <div class="earlier-media-grid">
      <figure class="earlier-media-card">
        <div class="earlier-media-frame earlier-media-frame--diagram">
          <img src="../assets/research/earlier/autonomous-driving-recognition-experiment.png" alt="Early autonomous-driving road-obstacle recognition experiment" loading="lazy">
        </div>
        <figcaption>Early autonomous-driving road-obstacle recognition experiment.</figcaption>
      </figure>
      <figure class="earlier-media-card">
        <div class="earlier-media-frame">
          <img src="../assets/research/earlier/path-tracking-demo.gif" alt="Path tracking and trajectory control demonstration" loading="lazy">
        </div>
        <figcaption>Path tracking and trajectory control demonstration.</figcaption>
      </figure>
      <figure class="earlier-media-card">
        <div class="earlier-media-frame">
          <iframe src="https://www.youtube-nocookie.com/embed/srNsl74nGyU" title="Intelligent vehicle-infrastructure cooperative system demonstration" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
        <figcaption>Location awareness and travel-mode classification demonstration.</figcaption>
      </figure>
      <figure class="earlier-media-card">
        <div class="earlier-media-frame">
          <iframe src="https://www.youtube-nocookie.com/embed/4dkykpWYjqo?start=58" title="RSSI vehicle positioning in tunnels and parking facilities demonstration" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
        <figcaption>RSSI vehicle positioning in tunnels and parking facilities.</figcaption>
      </figure>
    </div>
    <div class="related-publications">
      <p class="related-publications-label">Related Publications:</p>
      <ul class="related-publications-list">
        <li><a href="../publications/#huang2019wifi">A Novel WiFi-Oriented RSSI Signal Processing Method for Tracking Low-Speed Pedestrians</a> (ICTIS, 2019)</li>
        <li><a href="../publications/#huang2020wifi">Multi-Stage Pedestrian Positioning Using Filtered WiFi Scanner Data in an Urban Road Environment</a> (Sensors, 2020)</li>
        <li><a href="../publications/#lin2021rssi">RSSI Positioning Method of Vehicles in Tunnels Based on Semi-Supervised Extreme Learning Machine</a> (Journal of Traffic and Transportation Engineering, 2021)</li>
      </ul>
    </div>
  </div>

  <div class="past-research-group">
    <h5>Transportation Data Mining and Prediction</h5>
    <p class="past-research-period">2019–2021</p>
    <ul>
      <li><strong>Citywide Metro-to-Bus Transfer Analytics</strong>: I fused smart-card and GPS data to infer missing bus boarding stops and identify actual metro-to-bus interchange trips. Station-specific transfer-time thresholds were then used to evaluate connectivity and locate poorly connected transfer hubs.</li>
      <li><strong>Short-Term Traffic Speed Prediction with Attention-Based LSTM</strong>: I developed an integrated framework that combines missing-data preprocessing with attention-based traffic-speed prediction. Bayesian inference and dynamic time warping improve the raw data before the LSTM model captures temporal traffic patterns.</li>
      <li><strong>WiCL: Portable WiFi-Based Traffic Monitoring and Travel-Mode Recognition</strong>: I helped develop a low-cost, portable system that uses only WiFi scanner data for traffic monitoring and non-motorized travel-mode recognition. Signal filtering, feature extraction, and an LSTM classifier were combined to distinguish pedestrians from cyclists.</li>
    </ul>
    <div class="earlier-media-grid">
      <figure class="earlier-media-card">
        <div class="earlier-media-frame">
          <iframe src="https://www.youtube-nocookie.com/embed/gcR_oDDVYe4" title="Traffic data mining software demonstration" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
        <figcaption>DataFind traffic data-mining software demonstration.</figcaption>
      </figure>
    </div>
    <div class="related-publications">
      <p class="related-publications-label">Related Publications:</p>
      <ul class="related-publications-list">
        <li><a href="../publications/#huang2019metrobus">Citywide Metro-to-Bus Transfer Behavior Identification Based on Combined Data from Smart Cards and GPS</a> (Applied Sciences, 2019)</li>
        <li><a href="../publications/#wu2022metrobus">Recognizing Real-Time Transfer Patterns Between Metro and Bus Systems Based on Spatial–Temporal Constraints</a> (ASCE-JTE, 2022)</li>
        <li><a href="../publications/#wu2020lstm">A Combined Deep Learning Method with Attention-Based LSTM Model for Short-Term Traffic Speed Forecasting</a> (Journal of Advanced Transportation, 2020)</li>
        <li><a href="../publications/#xu2023wicl">Wi-CL: Low-Cost WiFi-Based Detection System for Nonmotorized Traffic Travel Mode Classification</a> (Journal of Advanced Transportation, 2023)</li>
      </ul>
    </div>
  </div>

  <div class="past-research-group">
    <h5>Digital Twin and Multi-Objective Optimization</h5>
    <p class="past-research-period">2016–2017</p>
    <ul>
      <li><strong>Digital-Twin Production-Line Design and Optimization</strong>: I combined physics-based system modeling with distributed real-time production data to support production-line design before deployment. An analytical decoupling framework provided engineering-analysis and multi-objective decision-support capabilities.</li>
    </ul>
    <div class="earlier-media-grid">
      <figure class="earlier-media-card">
        <div class="earlier-media-frame">
          <iframe src="https://www.youtube-nocookie.com/embed/UTap5pSXgrg" title="Digital twin-based hollow glass production line demonstration" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
        <figcaption>Digital twin-based hollow glass production-line demonstration.</figcaption>
      </figure>
    </div>
  </div>
</div>
</div>

<div class="research-prose">
<h4>Future Directions</h4>

<p>
  Looking ahead, I plan to develop embodied foundation models that can generalize across environments, embodiments, sensing configurations, and hardware while remaining grounded in physical constraints and human expectations. This direction will connect foundation-model reasoning with data-efficient adaptation and rigorous evaluation on real physical platforms.
</p>

<p>
  I also aim to build autonomous systems that can learn from physical interaction, failure discovery, and real-world feedback without weakening safety. By combining closed-loop simulation, real-world testing, and independent verification, I hope to make continuous improvement both practical and trustworthy.
</p>
</div>
