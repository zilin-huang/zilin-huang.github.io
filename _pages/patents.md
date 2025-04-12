---
layout: page
title: Patents
permalink: /patents/
description:
nav: true
nav_order: 8
---

<style>
/* 基础列表样式 */
.artistic-list {
  counter-reset: item;
  list-style-type: none;
  padding-left: 0;
}

.artistic-list li {
  position: relative;
  padding-left: 2.5em;
  margin-bottom: 1.5em;
  padding-bottom: 1em;
  border-bottom: 1px dashed rgba(var(--global-theme-color-rgb), 0.1);
  transition: all 0.3s ease;
}

.artistic-list li:last-child {
  border-bottom: none;
}

.artistic-list li:hover {
  background-color: rgba(var(--global-theme-color-rgb), 0.03);
  padding-left: 3em;
  border-radius: 4px;
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
  font-size: 1.1em;
  width: 1.8em;
  height: 1.8em;
  line-height: 1.8em;
  border-radius: 50%;
  background-color: var(--global-card-bg-color);
  color: var(--global-theme-color);
  text-align: center;
  box-shadow: 0 2px 4px var(--global-shadow-color);
  border: 1px solid rgba(var(--global-theme-color-rgb), 0.2);
  transition: all 0.3s ease;
}

.artistic-list li:hover:before {
  background-color: var(--global-theme-color);
  color: var(--global-bg-color);
  box-shadow: 0 3px 6px var(--global-shadow-color-hover);
  transform: scale(1.05);
}

/* 链接样式 */
.artistic-list a {
  color: var(--global-theme-color);
  text-decoration: none;
  transition: color 0.2s ease;
  display: inline-flex;
  align-items: center;
  font-weight: 500;
}

.artistic-list a:hover {
  color: var(--global-hover-color);
  text-decoration: underline;
}

.artistic-list a:after {
  content: "📄";
  margin-left: 5px;
  font-size: 0.9em;
}

/* 标题样式 */
h4 {
  position: relative;
  padding-bottom: 10px;
  margin-bottom: 20px;
  color: var(--global-text-color);
  font-size: 1.3em;
  font-weight: 600;
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
    padding-bottom: 1.2em;
    margin-bottom: 1.2em;
  }
  
  .artistic-list li:hover {
    padding-left: 2.2em;
  }
}
</style>

<h4 style="text-align: left;">Grant of Patent</h4>
<ol class="artistic-list">
<li><span class="patent-type invention">发明专利</span>A RSSI-based method for positioning low-speed moving vehicles.<br>
Yongjie Lin, <strong>Zilin Huang</strong>, and Lunhui Xu.<br>
<em>Chinese Invention Patent, Application Number: CN109375168A</em>. <a href="../assets/patents/patent_CN109375168A.pdf">PDF</a></li>

<li><span class="patent-type invention">发明专利</span>A RSSI-based method for positioning low-speed moving vehicles.<br>
Yongjie Lin, <strong>Zilin Huang</strong>, Sheng Zhao, Lunhui Xu, and Shanyu Tang.<br>
<em>Chinese Invention Patent, Application Number: CN201811368103.8</em>. <a href="../assets/patents/patent_CN201811368103.8.pdf">PDF</a></li>

<li><span class="patent-type invention">发明专利</span>Urban traffic operation evaluation method based on ecological index.<br>
Yongjie Lin, Weijia Zeng, Yanqing Yang, Yuming Cheng, Yuheng Liu, Haixia Guan, and <strong>Zilin Huang</strong>.<br>
<em>Chinese Invention Patent, Application Number: CN201911419439.7</em>. <a href="../assets/patents/patent_CN201911419439.7.pdf">PDF</a></li>

<li><span class="patent-type utility-model">实用新型</span>A device for counting the number of passengers getting on and off in a portable bus.<br>
<strong>Zilin Huang</strong>, Yongjie Lin, and Lunhui Xu.<br>
<em>Chinese Utility Model Patent, Application Number: CN201920581476.7</em>. <a href="../assets/patents/patent_CN201920581476.7.pdf">PDF</a></li>

<li><span class="patent-type utility-model">实用新型</span>RSSI-based road traffic jam detection and dispersion device.<br>
<strong>Zilin Huang</strong>, Yuzhuang Pian, Yongjie Lin, Pan Wu, and Yuqing Zhan.<br>
<em>Chinese Utility Model Patent, Application Number: CN202021751310.4</em>. <a href="../assets/patents/patent_CN202021751310.4.pdf">PDF</a></li>

<li><span class="patent-type utility-model">实用新型</span>Vehicle-mounted positioning device based on RSSI and inertial navigation.<br>
Yongjie Lin, <strong>Zilin Huang</strong>.<br>
<em>Chinese Utility Model Patent, Application Number: CN201920574767.3</em>. <a href="../assets/patents/patent_CN201920574767.3.pdf">PDF</a></li>

<li><span class="patent-type utility-model">实用新型</span>Micro device for positioning moving target based on RSSI.<br>
Yongjie Lin, <strong>Zilin Huang</strong>.<br>
<em>Chinese Utility Model Patent, Application Number: CN201920574719.4</em>. <a href="../assets/patents/patent_CN201920574719.4.pdf">PDF</a></li>

<li><span class="patent-type utility-model">实用新型</span>An obstacle avoidance system for unmanned vehicles based on machine vision and infrared sensors.<br>
Yongjie Lin, <strong>Zilin Huang</strong>, and Lunhui Xu.<br>
<em>Chinese Utility Model Patent, Application Number: CN202020235979.1</em>. <a href="../assets/patents/patent_CN202020235979.1.pdf">PDF</a></li>

<li><span class="patent-type utility-model">实用新型</span>Visual navigation system for assisting unmanned vehicles.<br>
Yongjie Lin, <strong>Zilin Huang</strong>, and Lunhui Xu.<br>
<em>Chinese Utility Model Patent, Application Number: CN202020235977.2</em>. <a href="../assets/patents/patent_CN202020235977.2.pdf">PDF</a></li>

<li><span class="patent-type utility-model">实用新型</span>A target intrusion detection device based on wireless communication signal.<br>
Yongjie Lin, <strong>Zilin Huang</strong>, and Lunhui Xu.<br>
<em>Chinese Utility Model Patent, Application Number: CN202020965272.6</em>. <a href="../assets/patents/patent_CN202020965272.6.pdf">PDF</a></li>

<li><span class="patent-type utility-model">实用新型</span>A RSSI-based positioning and early warning device for two-passenger and one-dangerous vehicles.<br>
Yuzhuang Pian, <strong>Zilin Huang</strong>, Yongjie Lin, Yuqing Zhan, and Pan Wu.<br>
<em>Chinese Utility Model Patent, Application Number: CN202021751321.2</em>. <a href="../assets/patents/patent_CN202021751321.2.pdf">PDF</a></li>

<li><span class="patent-type utility-model">实用新型</span>A kind of elevator apparatus of wheel.<br>
Chao He, Zhanqin Yu, Zequan Hong, Chengzhao Zhang, Ziping Chen, and <strong>Zilin Huang</strong>.<br>
<em>Chinese Utility Model Patent, Application Number: CN201620682753.X</em>. <a href="../assets/patents/patent_CN201620682753.X.pdf">PDF</a></li>

<li><span class="patent-type utility-model">实用新型</span>Tunnel vehicle accident detection and early warning device based on RSSI.<br>
Binrao, Zhihong Ye, Yongjie Lin, Haochuan Zhong, Yuqing Zhan, Jiajun Wu, Yuzhuang Pian, and <strong>Zilin Huang</strong>.<br>
<em>Chinese Invention Patent, Application Number: CN202120982224.2</em>. <a href="../assets/patents/patent_CN202120982224.2.pdf">PDF</a></li>
</ol>

<h4 style="text-align: left;">Substantive Examination</h4>
<ol class="artistic-list">
<li><span class="patent-type invention">发明专利</span>Subway transfer bus behavior identification method, system, computer equipment and storage medium.<br>
<strong>Zilin Huang</strong>, and Lunhui Xu.<br>
<em>Chinese Invention Patent, Application Number: CN201910051795.1</em>. <a href="../assets/patents/patent_CN201910051795.1.pdf">PDF</a></li>

<li><span class="patent-type invention">发明专利</span>The recognition methods of Metro Passenger time getting off, system, computer equipment and storage medium.<br>
<strong>Zilin Huang</strong>, and Lunhui Xu.<br>
<em>Chinese Invention Patent, Application Number: CN201910051785.8</em>. <a href="../assets/patents/patent_CN201910051785.8.pdf">PDF</a></li>

<li><span class="patent-type invention">发明专利</span>A kind of hot spot junction of park and shift recognition methods based on IC card data.<br>
<strong>Zilin Huang</strong>, and Lunhui Xu.<br>
<em>Chinese Invention Patent, Application Number: CN201910339482.6</em>. <a href="../assets/patents/patent_CN201910339482.6.pdf">PDF</a></li>

<li><span class="patent-type invention">发明专利</span>A kind of subway station passenger flow monitoring method and system.<br>
<strong>Zilin Huang</strong>, Yongjie Lin, and Lunhui Xu.<br>
<em>Chinese Invention Patent, Application Number: CN201910338991.7</em>. <a href="../assets/patents/patent_CN201910338991.7.pdf">PDF</a></li>

<li><span class="patent-type invention">发明专利</span>A kind of traffic trip mode identification method based on wireless signal.<br>
Yongjie Lin, <strong>Zilin Huang</strong>.<br>
<em>Chinese Invention Patent, Application Number: CN201910581470.4</em>. <a href="../assets/patents/patent_CN201910581470.4.pdf">PDF</a></li>
</ol>

<h4 style="text-align: left;">Computer Software Copyright</h4>
<ol class="artistic-list">
<li><span class="patent-type software">软件著作权</span>The Simulation System of Rapid Customization Design Platform for Hollow Glass Automatic Production Line V1.0<br>
Kuanyuan Li, <strong>Zilin Huang</strong>, Luofang, and Chuang Zhou.<br>
<em>Chinese Computer Software Copyright, Application Number: 2017SR099863; Legal Status: Authorization</em>.</li>

<li><span class="patent-type software">软件著作权</span>Intelligent Workshop Rapid Customization Design Platform System V1.0<br>
Xiaoping Li, Luo Fang, <strong>Zilin Huang</strong>, and Chuang Zhou.<br>
<em>Chinese Computer Software Copyright, Application Number: 2017SR302066; Legal Status: Authorization</em>.</li>

<li><span class="patent-type software">软件著作权</span>Student Organization Activity Approval System V1.0<br>
Junxing Zhang, Ruixuan Cai, Huanzeng Yang, <strong>Zilin Huang</strong>, Poyu Zhuang, Guangzheng Zhong, and Jiahao Jiang.<br>
<em>Chinese Computer Software Copyright, Application Number: 2017SR099823; Legal Status: Authorization</em>.</li>

<li><span class="patent-type software">软件著作权</span>Club Activities Background Management System V1.0<br>
Junxing Zhang, Huanzeng Yang, Poyu Zhuang, <strong>Zilin Huang</strong>, Guangzheng Zhong, and Jiahao Jiang.<br>
<em>Chinese Computer Software Copyright, Application Number: 2017SR302060; Legal Status: Authorization</em>.</li>
</ol>