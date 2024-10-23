---
layout: page
permalink: /publications/
title: Publications
description: 
years: [2024,2023,2022,2021,2020]
nav: true
nav_order: 2
---

<span style="display: inline-block; font-size: 1.2em;">
  For a complete list of publications, please refer to&nbsp;
  <a href="https://scholar.google.com/citations?user=DPN2wc4AAAAJ&hl=zh-CN&oi=ao" target="_blank">
    <img src="../assets/img/icon/google-scholar-logo.png" alt="Google Scholar" width="28" height="28" style="vertical-align: middle;">
  </a>
</span>




---

<h2>Selected Publications</h2>

<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <!-- <h2 class="year">{{y}}</h2>    -->
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>