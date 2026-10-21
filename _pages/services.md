---
layout: page
title: Services
permalink: /services/
description: 
nav: true
nav_order: 8
---

<style>
/* 基础样式 */
.services-container {
  margin-bottom: 20px;
}

.conference-item {
  padding: 15px 0px 5px 0px;
  margin-bottom: 5px;
  border-bottom: 1px dashed rgba(var(--global-theme-color-rgb), 0.1);
}

.conference-item:last-child {
  border-bottom: none;
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

.reviewer-list {
  columns: 2;
  column-gap: 2.5rem;
}

.reviewer-list li {
  break-inside: avoid;
}

.service-date {
  margin-left: 5px;
  color: var(--global-text-color-light);
  font-size: 0.9em;
  white-space: nowrap;
}

.conference-gallery {
  margin-bottom: 0;
}

.conference-gallery p {
  margin-bottom: 0;
}

.conference-gallery > .col-md-4 {
  flex: 0 0 30%;
  max-width: 30%;
}

.conference-gallery > .col-md-4 img {
  height: 190px !important;
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
  background: var(--global-theme-color);
  border-radius: 3px;
}

h5 {
  margin-top: 5px;
  margin-bottom: 10px;
  color: var(--global-theme-color);
  font-size: 1.1em;
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
  .conference-gallery > .col-md-4 {
    flex: 0 0 100%;
    max-width: 100%;
  }

  .conference-gallery > .col-md-4 img {
    height: auto !important;
    max-height: 320px;
  }

  .reviewer-list {
    columns: 1;
  }

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

<h4 style="text-align: left;">Editorial &amp; Peer-Review Service</h4>

<div class="services-container">
  <h5 style="text-align: left;">Journal Review</h5>
  <ul class="services-list academic-services reviewer-list">
    <li>Nature Communications</li>
    <li>IEEE Transactions on Intelligent Transportation Systems (TITS)</li>
    <li>IEEE Transactions on Vehicular Technology (TVT)</li>
    <li>Accident Analysis and Prevention (AAP)</li>
    <li>IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)</li>
    <li>IEEE Transactions on Cognitive and Developmental Systems (TCDS)</li>
    <li>IEEE Transactions on Intelligent Vehicles (TIV)</li>
    <li>Transportation Research Part C: Emerging Technologies (Part C)</li>
    <li>Computer-Aided Civil and Infrastructure Engineering (CACAIE)</li>
    <li>IEEE Transactions on Image Processing (TIP)</li>
    <li>IEEE Robotics and Automation Letters (RA-L)</li>
    <li>Expert Systems With Applications</li>
    <li>Applied Soft Computing Journal (ASOC)</li>
    <li>IEEE Intelligent Transportation Systems Magazine (ITSM)</li>
    <li>Journal of Advanced Transportation (JAT) <a href="{{ '/assets/services/2024_ATR_Reviewer_Certificate.pdf' | relative_url }}" target="_blank">[Certificate]</a></li>
    <li>Neural Computing and Applications (NCAA)</li>
    <li>Sensors</li>
    <li>IEEE Access</li>
    <li>Applied Intelligence</li>
    <li>Scientific Reports</li>
  </ul>
</div>

<div class="services-container">
  <h5 style="text-align: left;">Conference Review</h5>
  <ul class="services-list academic-services">
    <li>Transportation Research Board Annual Meeting (TRB)</li>
    <li>IEEE Intelligent Vehicles Symposium (IV)</li>
    <li>IEEE Intelligent Transportation Systems Conference (ITSC)</li>
  </ul>
</div>

<h4 style="text-align: left;">Conference Service</h4>

<div class="services-container">
  <h5 style="text-align: left;">Organization &amp; Session Leadership</h5>
  <ul class="services-list community-services" style="margin-bottom: 5px;">
    <li class="conference-item">Workshop Organizer, 3rd Workshop on Multi-Agent Embodied Intelligent Systems Meet Generative-AI Era: Opportunities, Challenges and Futures (MEIS @ CVPR 2026), Denver, CO, US, Jun 4 2026 <a href="https://coop-intelligence.github.io/" target="_blank" rel="noopener noreferrer">[Website]</a></li>
    <li class="conference-item">Committee Chair, 5th Annual Conference on Next-Generation Transport Systems (NGTS 2026), West Lafayette, IN, US, May 22 2026 <a href="https://nextranspurdue.wixsite.com/ngts5/copy-of-organizing-committee" target="_blank" rel="noopener noreferrer">[Website]</a></li>
  </ul>
  <div class="row conference-gallery" style="margin-top: 5px;">
    <div class="col-md-4">
      <img class="img-fluid rounded z-depth-1" src="/assets/services/2026%20NGTS/ngts-student-team.webp" srcset="/assets/services/2026%20NGTS/ngts-student-team-900.webp 900w, /assets/services/2026%20NGTS/ngts-student-team-1600.webp 1600w, /assets/services/2026%20NGTS/ngts-student-team.webp 3200w" sizes="(max-width: 767px) 100vw, (max-width: 1199px) 33vw, 445px" alt="Student team at NGTS 2026" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        Student team at NGTS 2026
      </p>
    </div>
    <div class="col-md-4">
      <img class="img-fluid rounded z-depth-1" src="/assets/services/2026%20NGTS/ngts-organizing-committee.webp" srcset="/assets/services/2026%20NGTS/ngts-organizing-committee-900.webp 900w, /assets/services/2026%20NGTS/ngts-organizing-committee.webp 1619w" sizes="(max-width: 767px) 100vw, (max-width: 1199px) 33vw, 445px" alt="NGTS 2026 organizing committee" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        NGTS 2026 organizing committee
      </p>
    </div>
  </div>
  <ul class="services-list community-services" style="margin-bottom: 5px;">
    <li class="conference-item">Workshop Organizer, Modified Asphalt Research Center (MARC) Future Research Focus Workshop, Madison, WI, US, Feb 21 2024 <a href="{{ '/assets/services/MARC/2024_MARC_1.jpg' | relative_url }}" target="_blank">[Flyer]</a></li>
  </ul>
  <div class="row conference-gallery" style="margin-top: 5px;">
    <div class="col-md-4">
      <img class="img-fluid rounded z-depth-1" src="../assets/services/MARC/2024_MARC_4.jpg" srcset="../assets/services/MARC/2024_MARC_4-thumb-900.webp 900w, ../assets/services/MARC/2024_MARC_4-thumb-1600.webp 1600w" sizes="(max-width: 768px) 100vw, 33vw" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        MARC Workshop
      </p>
    </div>
    <div class="col-md-4">
      <img class="img-fluid rounded z-depth-1" src="../assets/services/MARC/2024_MARC_5.jpg" srcset="../assets/services/MARC/2024_MARC_5-thumb-900.webp 900w, ../assets/services/MARC/2024_MARC_5-thumb-1600.webp 1600w" sizes="(max-width: 768px) 100vw, 33vw" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        MARC Workshop
      </p>
    </div>
  </div>
  <ul class="services-list community-services" style="margin-top: 0; margin-bottom: 5px;">
    <li class="conference-item">Session Chair, 3rd Annual Conference on Next-Generation Transport Systems (NGTS-3), West Lafayette, IN, US, May 16-18 2023 <a href="{{ '/assets/services/NGTS/2023_NGTS_Flyer.pdf' | relative_url }}" target="_blank">[Flyer]</a></li>
  </ul>
  <div class="row conference-gallery" style="margin-top: 5px;">
    <div class="col-md-4">
      <img class="img-fluid rounded z-depth-1" src="../assets/services/NGTS/2023_NGTS_1.jpg" srcset="../assets/services/NGTS/2023_NGTS_1-thumb-900.webp 900w, ../assets/services/NGTS/2023_NGTS_1-thumb-1600.webp 1600w" sizes="(max-width: 768px) 100vw, 33vw" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        NGTS-3 Conference
      </p>
    </div>
    <div class="col-md-4">
      <img class="img-fluid rounded z-depth-1" src="../assets/services/NGTS/2023_NGTS_2.jpg" style="width: 100%; height: 220px; object-fit: cover;" loading="lazy">
      <p style="text-align: center; margin-top: 10px; color: var(--global-text-color-light); font-size: 0.9em;">
        NGTS-3 Conference
      </p>
    </div>
  </div>
</div>

<h4 style="text-align: left;">Professional Memberships</h4>

<div class="services-container">
  <ul class="services-list academic-services">
    <li>IEEE Student Member</li>
    <li>ASCE Student Member</li>
    <li>COTA Student Member</li>
  </ul>
</div>

<h4 style="text-align: left;">Leadership &amp; Outreach</h4>

<div class="services-container">
  <h5 style="text-align: left;">Student Leadership</h5>
  <ul class="services-list community-services">
    <li>Member, Graduate Student Union <span class="service-date">(Oct 2018–Oct 2019)</span></li>
    <li>Member, Student Leader Advocacy Team of Guangdong Province <span class="service-date">(Oct 2017–Oct 2018)</span></li>
    <li>Deputy Secretary, Student Government <span class="service-date">(Dec 2016–May 2018)</span><br><span style="color: var(--global-text-color-light); font-size: 0.9em;">Assisted with community-service activities and academic competitions.</span></li>
    <li>Member, Student Union of Guangdong Province <span class="service-date">(Apr 2016–May 2018)</span></li>
    <li>Tutor Assistant, School of Mechanical and Electrical Engineering <span class="service-date">(Sep 2015–Sep 2016)</span></li>
    <li>Freshman Class Assistant, School of Mechanical and Electrical Engineering <span class="service-date">(Sep 2015–Sep 2016)</span></li>
    <li>Class Leader, School of Mechanical and Electrical Engineering <span class="service-date">(Sep 2014–Sep 2015)</span></li>
  </ul>
</div>

<div class="services-container">
  <h5 style="text-align: left;">Outreach &amp; Volunteering</h5>
  <ul class="services-list community-services">
    <li>Invited Guest Speaker, Youth Science Camp for Chinese Universities <span class="service-date">(Jul 2018)</span></li>
    <li>Founder, Transformation Program <span class="service-date">(Apr 2018)</span></li>
    <li>Outstanding Community Worker, Summer Rural Social Practice Program, Guangdong Province <span class="service-date">(Sep 2017)</span></li>
    <li>Volunteer, Guangzhou Export Commodities Fair <span class="service-date">(Nov 2016)</span></li>
    <li>Outstanding Community Worker, Summer Rural Social Practice Program, China <span class="service-date">(Sep 2016)</span></li>
  </ul>
</div>
