---
layout: page
title: Products
permalink: /products/
description:
nav: true
nav_order: 5
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

<h4>Technology Transfer</h4>

<!-- <p style="text-align: justify;">
  Growing up in Shenzhen, China, I witnessed the city's remarkable transformation from a small fishing village into a global technology hub - what many call the "Shenzhen speed." This environment planted the seeds of entrepreneurial spirit in me from an early age. During high school, I ventured into selling phone cards, coordinating food delivery services for school, setting up market stalls, selling courses, and organizing the campus laundry market. These experiences laid the foundation for my understanding of business models. 
</p> -->
  
<p style="text-align: justify;">  
I am deeply passionate about bridging the gap between scientific discovery and real-world impact. Before beginning my Ph.D. journey, <b>I founded two technology companies</b> in China, aiming to transform my research findings into practical solutions. Through this experience, I had the opportunity to collaborate with industry professionals and gain valuable insights into the innovation ecosystem. Encouragingly, the companies attracted <b>over 3 million RMB</b> in potential investment from leading institutions such as <b>Yueke Securities</b> and <b>CITIC Securities</b>. These experiences reinforced my belief that when scientific discoveries move beyond the lab and into society, they can generate meaningful and lasting value.
</p>

<!-- Entrepreneurship images -->
<div class="row">
  <div class="col-md-4 mt-3">
    <img class="img-fluid rounded z-depth-1" src="../assets/personal/entrepreneurship/2021-qinglan-3.jpg" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
    <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
      Qinglan Project (2021)
    </p>
  </div>
  <div class="col-md-4 mt-3">
    <img class="img-fluid rounded z-depth-1" src="../assets/personal/entrepreneurship/2021-qinglan-4.jpg" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
    <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
      Qinglan Project (2021)
    </p>
  </div>
  <div class="col-md-4 mt-3">
    <img class="img-fluid rounded z-depth-1" src="../assets/personal/entrepreneurship/2020-wininguangdong-2.jpg" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
    <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
      Winning Guangdong Competition (2020)
    </p>
  </div>
</div>

<div class="row mt-1">
  <div class="col-md-4 mt-3">
    <img class="img-fluid rounded z-depth-1" src="../assets/personal/entrepreneurship/2020-wininguangdong-4.jpg" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
    <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
      Winning Guangdong Competition (2020)
    </p>
  </div>
  <div class="col-md-4 mt-3">
    <img class="img-fluid rounded z-depth-1" src="../assets/personal/entrepreneurship/2020-wininguangdong-6.png" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
    <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
      Winning Guangdong Competition (2020)
    </p>
  </div>
  <div class="col-md-4 mt-3">
    <img class="img-fluid rounded z-depth-1" src="../assets/personal/entrepreneurship/2020-chuangkeguangdong-2.jpg" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
    <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
      Chuangke Guangdong Competition (2020)
    </p>
  </div>
</div>

<div class="row mt-1">
  <div class="col-md-4 mt-3">
    <img class="img-fluid rounded z-depth-1" src="../assets/personal/entrepreneurship/2020-chuangkeguangdong-3.jpg" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
    <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
      Chuangke Guangdong Competition (2020)
    </p>
  </div>
</div>


<h4>Patents Property</h4>

<div class="research-area">
<h5>Grant of Patent</h5>
<ol class="artistic-list">
<li><span class="patent-type invention">发明专利</span>A RSSI-based method for positioning low-speed moving vehicles. <a href="../assets/patents/patent_CN109375168A.pdf" target="_blank">PDF</a><br>
Yongjie Lin, <strong>Zilin Huang</strong>, and Lunhui Xu. <em>Invention Patent, CN109375168A</em>.</li>

<li><span class="patent-type invention">发明专利</span>A RSSI-based method for positioning low-speed moving vehicles. <a href="../assets/patents/patent_CN201811368103.8.pdf" target="_blank">PDF</a><br>
Yongjie Lin, <strong>Zilin Huang</strong>, Sheng Zhao, Lunhui Xu, and Shanyu Tang. <em>Invention Patent, CN201811368103.8</em>.</li>

<li><span class="patent-type invention">发明专利</span>Urban traffic operation evaluation method based on ecological index. <a href="../assets/patents/patent_CN201911419439.7.pdf" target="_blank">PDF</a><br>
Yongjie Lin, Weijia Zeng, Yanqing Yang, Yuming Cheng, Yuheng Liu, Haixia Guan, and <strong>Zilin Huang</strong>. <em>Invention Patent, CN201911419439.7</em>.</li>

<li><span class="patent-type utility-model">实用新型</span>A device for counting the number of passengers getting on and off in a portable bus. <a href="../assets/patents/patent_CN201920581476.7.pdf" target="_blank">PDF</a><br>
<strong>Zilin Huang</strong>, Yongjie Lin, and Lunhui Xu. <em>Utility Model Patent, CN201920581476.7</em>.</li>

<li><span class="patent-type utility-model">实用新型</span>RSSI-based road traffic jam detection and dispersion device. <a href="../assets/patents/patent_CN202021751310.4.pdf" target="_blank">PDF</a><br>
<strong>Zilin Huang</strong>, Yuzhuang Pian, Yongjie Lin, Pan Wu, and Yuqing Zhan. <em>Utility Model Patent, CN202021751310.4</em>.</li>

<li><span class="patent-type utility-model">实用新型</span>Vehicle-mounted positioning device based on RSSI and inertial navigation. <a href="../assets/patents/patent_CN201920574767.3.pdf" target="_blank">PDF</a><br>
Yongjie Lin, <strong>Zilin Huang</strong>. <em>Utility Model Patent, CN201920574767.3</em>.</li>

<li><span class="patent-type utility-model">实用新型</span>Micro device for positioning moving target based on RSSI. <a href="../assets/patents/patent_CN201920574719.4.pdf" target="_blank">PDF</a><br>
Yongjie Lin, <strong>Zilin Huang</strong>. <em>Utility Model Patent, CN201920574719.4</em>.</li>

<li><span class="patent-type utility-model">实用新型</span>An obstacle avoidance system for unmanned vehicles based on machine vision and infrared sensors. <a href="../assets/patents/patent_CN202020235979.1.pdf" target="_blank">PDF</a><br>
Yongjie Lin, <strong>Zilin Huang</strong>, and Lunhui Xu. <em>Utility Model Patent, CN202020235979.1</em>.</li>

<li><span class="patent-type utility-model">实用新型</span>Visual navigation system for assisting unmanned vehicles. <a href="../assets/patents/patent_CN202020235977.2.pdf" target="_blank">PDF</a><br>
Yongjie Lin, <strong>Zilin Huang</strong>, and Lunhui Xu. <em>Utility Model Patent, CN202020235977.2</em>.</li>

<li><span class="patent-type utility-model">实用新型</span>A target intrusion detection device based on wireless communication signal. <a href="../assets/patents/patent_CN202020965272.6.pdf" target="_blank">PDF</a><br>
Yongjie Lin, <strong>Zilin Huang</strong>, and Lunhui Xu. <em>Utility Model Patent, CN202020965272.6</em>.</li>

<li><span class="patent-type utility-model">实用新型</span>A RSSI-based positioning and early warning device for two-passenger and one-dangerous vehicles. <a href="../assets/patents/patent_CN202021751321.2.pdf" target="_blank">PDF</a><br>
Yuzhuang Pian, <strong>Zilin Huang</strong>, Yongjie Lin, Yuqing Zhan, and Pan Wu. <em>Utility Model Patent, CN202021751321.2</em>.</li>

<li><span class="patent-type utility-model">实用新型</span>A kind of elevator apparatus of wheel. <a href="../assets/patents/patent_CN201620682753.X.pdf" target="_blank">PDF</a><br>
Chao He, Zhanqin Yu, Zequan Hong, Chengzhao Zhang, Ziping Chen, and <strong>Zilin Huang</strong>. <em>Utility Model Patent, CN201620682753.X</em>.</li>

<li><span class="patent-type utility-model">实用新型</span>Tunnel vehicle accident detection and early warning device based on RSSI. <a href="../assets/patents/patent_CN202120982224.2.pdf" target="_blank">PDF</a><br>
Binrao, Zhihong Ye, Yongjie Lin, Haochuan Zhong, Yuqing Zhan, Jiajun Wu, Yuzhuang Pian, and <strong>Zilin Huang</strong>. <em>Invention Patent, CN202120982224.2</em>.</li>
</ol>

<div class="research-area">
<h5>Substantive Examination</h5>
<ol class="artistic-list">
<li><span class="patent-type invention">发明专利</span>Subway transfer bus behavior identification method, system, computer equipment and storage medium. <a href="../assets/patents/patent_CN201910051795.1.pdf" target="_blank">PDF</a><br>
<strong>Zilin Huang</strong>, and Lunhui Xu. <em>Invention Patent, CN201910051795.1</em>.</li>

<li><span class="patent-type invention">发明专利</span>The recognition methods of Metro Passenger time getting off, system, computer equipment and storage medium. <a href="../assets/patents/patent_CN201910051785.8.pdf" target="_blank">PDF</a><br>
<strong>Zilin Huang</strong>, and Lunhui Xu. <em>Invention Patent, CN201910051785.8</em>.</li>

<li><span class="patent-type invention">发明专利</span>A kind of hot spot junction of park and shift recognition methods based on IC card data. <a href="../assets/patents/patent_CN201910339482.6.pdf" target="_blank">PDF</a><br>
<strong>Zilin Huang</strong>, and Lunhui Xu. <em>Invention Patent, CN201910339482.6</em>.</li>

<li><span class="patent-type invention">发明专利</span>A kind of subway station passenger flow monitoring method and system. <a href="../assets/patents/patent_CN201910338991.7.pdf" target="_blank">PDF</a><br>
<strong>Zilin Huang</strong>, Yongjie Lin, and Lunhui Xu. <em>Invention Patent, CN201910338991.7</em>.</li>

<li><span class="patent-type invention">发明专利</span>A kind of traffic trip mode identification method based on wireless signal. <a href="../assets/patents/patent_CN201910581470.4.pdf" target="_blank">PDF</a><br>
Yongjie Lin, <strong>Zilin Huang</strong>. <em>Invention Patent, CN201910581470.4</em>.</li>
</ol>

<div class="research-area">
<h5>Computer Software Copyright</h5>
<ol class="artistic-list">
<li><span class="patent-type software">软件著作权</span>The Simulation System of Rapid Customization Design Platform for Hollow Glass Automatic Production Line V1.0<br>
Kuanyuan Li, <strong>Zilin Huang</strong>, Luofang, and Chuang Zhou. <em>Computer Software Copyright, 2017SR099863; Legal Status: Authorization</em>.</li>

<li><span class="patent-type software">软件著作权</span>Intelligent Workshop Rapid Customization Design Platform System V1.0<br>
Xiaoping Li, Luo Fang, <strong>Zilin Huang</strong>, and Chuang Zhou. <em>Computer Software Copyright, 2017SR302066; Legal Status: Authorization</em>.</li>

<li><span class="patent-type software">软件著作权</span>Student Organization Activity Approval System V1.0<br>
Junxing Zhang, Ruixuan Cai, Huanzeng Yang, <strong>Zilin Huang</strong>, Poyu Zhuang, Guangzheng Zhong, and Jiahao Jiang. <em>Computer Software Copyright, 2017SR099823; Legal Status: Authorization</em>.</li>

<li><span class="patent-type software">软件著作权</span>Club Activities Background Management System V1.0<br>
Junxing Zhang, Huanzeng Yang, Poyu Zhuang, <strong>Zilin Huang</strong>, Guangzheng Zhong, and Jiahao Jiang. <em>Computer Software Copyright, 2017SR302060; Legal Status: Authorization</em>.</li>
</ol>
</div>

