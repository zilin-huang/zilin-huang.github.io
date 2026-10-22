---
layout: page
permalink: /research/
title: Research
description: 
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
  margin-bottom: 14px;
  border-bottom: 1px dashed rgba(var(--global-theme-color-rgb), 0.1);
  padding-bottom: 10px;
}

.research-area:last-child {
  border-bottom: none;
}

.research-area h5 {
  color: var(--global-theme-color);
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

.project-links {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
}

.project-links a,
.project-links span {
  display: inline-block;
  padding: 4px 10px;
  border: 1px solid rgba(var(--global-theme-color-rgb), 0.25);
  border-radius: 999px;
  background: rgba(var(--global-theme-color-rgb), 0.06);
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

.research-prose {
  max-width: 100%;
  margin-left: auto;
  margin-right: auto;
}

.research-framework img {
  width: 90%;
  max-width: 1120px;
}

@media (max-width: 768px) {
  .research-framework img {
    width: 100%;
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

<div class="research-prose">
<h4>Research Vision</h4>

<p>
  My research interests lie at the intersection of <strong>Physical AI</strong> and <strong>human-centered transportation systems</strong>. I envision future mobility as a <strong>human–robot–society ecosystem</strong>, where humans coexist, interact, and collaborate with diverse autonomous agents, including self-driving vehicles, delivery robots, drones, and other embodied systems. To thrive in such environments, these agents must understand complex physical and social contexts, reason about their actions, adapt to human preferences and social norms, and operate safely and reliably under open-world uncertainty.
</p>

<p>
  My long-term goal is to develop <strong>Human-centered and Trustworthy Autonomous Systems (HEART)</strong> that can safely learn, interact, and collaborate with people in the physical world.
</p>
</div>

<div class="research-framework" style="text-align: center;">
  <img src="../../assets/research/visionfull.jpg" alt="Research framework for Human-centered and Trustworthy Autonomous Systems" style="border-radius: 8px;"/>
</div>

<div class="research-prose">
<h4>Research Theme 1: Human-Aware Intelligence and Decision-Making</h4>

<div class="research-area">
  <p class="theme-question">How can autonomous agents understand complex physical and social environments and make safe, reliable, and human-aware decisions?</p>
  <p>I integrate human-guided reinforcement learning, physics-informed feedback, and foundation-model-based semantic reasoning to provide meaningful supervision for safer and more intelligent autonomous behavior.</p>
  <div class="project-links">
    <a href="https://zilin-huang.github.io/HAIM-DRL-website/" target="_blank">HAIM-DRL</a>
    <a href="https://www.huang-zilin.com/PE-RLHF-website/" target="_blank">PE-RLHF</a>
    <a href="https://www.huang-zilin.com/VLM-RL-website/" target="_blank">VLM-RL</a>
    <a href="https://arxiv.org/abs/2602.10458" target="_blank">Found-RL</a>
  </div>
</div>

<h4>Research Theme 2: Generalization, Adaptation, and Real-World Deployment</h4>

<div class="research-area">
  <p class="theme-question">How can capabilities learned in simulation or encoded in foundation models generalize, adapt, and transfer to real physical systems?</p>
  <p>I investigate deployment gaps, model selection, data-efficient adaptation, and evaluation across environments, embodiments, sensing configurations, and physical platforms.</p>
  <div class="project-links">
    <a href="https://arxiv.org/abs/2604.03497" target="_blank">Sim2Real-AD</a>
    <a href="https://arxiv.org/abs/2603.18315" target="_blank">DriveVLM-RL</a>
    <span>TRIAGE</span>
    <span>DOSE</span>
    <span>ExecGap</span>
  </div>
</div>

<h4>Research Theme 3: Safe Continuous Improvement and Evaluation</h4>

<div class="research-area">
  <p class="theme-question">How can autonomous agents safely and continuously improve through physical interaction, failure discovery, and real-world feedback?</p>
  <p>I explore closed-loop testing, independent evaluation designed to resist reward hacking, and verifiable policy improvement under limited real-world testing budgets.</p>
  <div class="project-links">
    <a href="https://arxiv.org/abs/2504.18010" target="_blank">Sky-Drive</a>
    <span>Sealed-Loop</span>
    <span>RoadCert</span>
  </div>
</div>
</div>

<h4>Research Platforms</h4>

<div class="research-area">
  <h5>Sky-Drive Simulation Platform</h5>
  <p>
    Existing simulators often optimize traffic flow or validate a single vehicle, but lack distributed, multi-agent support. To address this gap, my colleagues and I at Sky-Lab developed Sky-Drive—a long-term effort with many contributors; I have been involved since Summer 2023. Sky-Drive integrates Unreal Engine/CARLA, ROS, WebSocket, and custom scenario pipelines to run synchronized simulations across multiple terminals. Unlike single-vehicle or flow-only tools, Sky-Drive emphasizes synchronized interactions among pedestrians, human-driven vehicles (HVs), and autonomous vehicles (AVs), and supports multi-participant intervention and co-study for human-AI collaborative driving research.
  </p>
  <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-top: 10px;">
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

<div class="research-area">
  <h5>Autonomous Vehicle Testbed</h5>
  <p>
     While simulation is safe and scalable, the sim-to-real gap remains a core challenge. At Sky-Lab, we maintain a real-world testbed that I actively use with my colleagues to validate human-centered AI algorithms. Our primary platform is a retrofit electric Ford E-Transit with a full autonomy stack: drive-by-wire, a multi-modal sensor suite (3 LiDARs, 7 cameras, radar), 5G connectivity (NETGEAR Nighthawk M6 Pro), and on-board GPU computing (RTX A6000). We also deploy portable RSUs/OBUs (e.g., Siemens RSUs, Cohda MK6C) and configurable traffic signals to create intersection and corridor scenarios. Combined with Sky-Lab’s Lambda servers (RTX Pro 6000, A6000, 4090, 4080), this cyber-physical setup lets me run end-to-end evaluations, collect edge cases, and iterate quickly on model design and safety checks in real traffic conditions.
  </p>
  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-top: 20px;">
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV1.png" alt="Autonomous Vehicle Testbed 1" style="width: 100%; height: 300px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Autonomous Van with Sensor Suite
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV3.png" alt="Autonomous Vehicle Testbed 2" style="width: 100%; height: 300px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Driver Cockpit and Control Interface
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV2.png" alt="Autonomous Vehicle Testbed 3" style="width: 100%; height: 300px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Computing Hardware
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV4.jpg" alt="Autonomous Vehicle Testbed 4" style="width: 100%; height: 300px; object-fit: cover; object-position: top;" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Portable Traffic Light
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV5.jpg" srcset="../assets/research/testbed/AV5-thumb-900.webp 900w, ../assets/research/testbed/AV5-thumb-1600.webp 1600w" sizes="(max-width: 768px) 100vw, 33vw" alt="Autonomous Vehicle Testbed 5" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Testbed
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV6.jpg" alt="Autonomous Vehicle Testbed 6" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        Sensor Configuration
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV8.png" alt="Autonomous Vehicle Testbed 8" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        V2X Experiment Equipment
      </p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <img class="img-fluid rounded z-depth-1" src="../assets/research/testbed/AV7.png" alt="Autonomous Vehicle Testbed 7" style="width: 100%; height: 200px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 8px; color: var(--global-text-color-light); font-size: 0.85em;">
        5G mmWave Mobile Hotspot
      </p>
    </div>
  </div>

  <div class="platform-subsection">
  <h6>End-to-End Autonomous Driving</h6>
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
        Live demo at 2025 AAA Safe Mobility Conference, Madison, WI.
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
<h4>Future Directions</h4>

<p>
  Looking ahead, I plan to develop embodied foundation models that can generalize across environments, embodiments, sensing configurations, and hardware while remaining grounded in physical constraints and human expectations. This direction will connect foundation-model reasoning with data-efficient adaptation and rigorous evaluation on real physical platforms.
</p>

<p>
  I also aim to build autonomous systems that can learn from physical interaction, failure discovery, and real-world feedback without weakening safety. By combining closed-loop simulation, real-world testing, and independent verification, I hope to make continuous improvement both practical and trustworthy.
</p>
</div>
