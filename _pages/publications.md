---
layout: page
permalink: /publications/
title: Publications
description: 
years: [2025, 2024]
nav: true
nav_order: 2
---

The list below may not be up to date, please check <a href="https://scholar.google.com/citations?user=RgO7ppoAAAAJ&hl=en">Google Scholar</a> for my latest publications.

---

<div class="publications">
{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}] %}
{% endfor %}
</div>