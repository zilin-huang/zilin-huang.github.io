---
layout: page
permalink: /publications/
title: Publications
description: "Peer-reviewed publications on intelligent transportation, autonomous driving, and human–AI collaboration."
years: [2026, 2025, 2024, 2023, 2022, 2021, 2020, 2019]
nav: true
nav_order: 3
---

<style>
/* Year navigation sidebar styles */
.year-nav {
  position: fixed;
  left: 40px;
  top: 50%;
  transform: translateY(-50%);
  background-color: white;
  padding: 15px;
  border-radius: 12px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  border: 1px solid rgba(var(--global-theme-color-rgb), 0.15);
}

.year-nav a {
  display: block;
  padding: 8px 25px;
  margin: 6px 0;
  color: var(--global-theme-color);
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.2s ease;
  font-size: 1em;
  text-align: center;
  position: relative;
  background-color: transparent;
}

.year-nav a:hover {
  background-color: rgba(var(--global-theme-color-rgb), 0.1);
}

.year-nav a.active {
  background-color: var(--global-theme-color);
  color: white;
  font-weight: 500;
}

.publication-year-section {
  scroll-margin-top: 100px;
}

.publication-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 12px 0 14px;
}

.publication-filter {
  padding: 5px 14px;
  border: 1px solid rgba(var(--global-theme-color-rgb), 0.3);
  border-radius: 999px;
  background: transparent;
  color: var(--global-theme-color);
  font: inherit;
  line-height: 1.4;
  cursor: pointer;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.publication-filter:hover,
.publication-filter.active {
  background: var(--global-theme-color);
  color: white;
}

.author-note {
  display: block;
  margin: 12px 0 6px;
  color: var(--global-text-color-light);
  font-size: 0.9em;
}

.publications {
  margin-top: 0.5rem;
}

.publication-year-section:first-child h2.year {
  margin-top: 0.75rem;
  padding-top: 0.5rem;
}

@media (max-width: 768px) {
  .year-nav {
    display: none;
  }
}
</style>

<!-- Year navigation sidebar -->
{% assign publication_years = site.data.publication_years | default: page.years %}
<div class="year-nav">
  {% for y in publication_years %}
    <a href="#year-{{y}}">{{y}}</a>
  {% endfor %}
</div>

For citation metrics and the latest updates, please visit my <a href="https://scholar.google.com/citations?user=RgO7ppoAAAAJ&hl=en">Google Scholar</a> profile.

<div class="publication-filters" role="group" aria-label="Filter publications">
  <button type="button" class="publication-filter active" data-filter="all" aria-pressed="true">All</button>
  <button type="button" class="publication-filter" data-filter="selected" aria-pressed="false">Selected</button>
  <button type="button" class="publication-filter" data-filter="journal" aria-pressed="false">Journal</button>
  <button type="button" class="publication-filter" data-filter="conference" aria-pressed="false">Conference</button>
  <button type="button" class="publication-filter" data-filter="preprint" aria-pressed="false">Preprint</button>
</div>

---

<span class="author-note"><sup>+</sup> Equal contribution; <sup>*</sup> Corresponding author.</span>

<div class="publications">
{% for y in publication_years %}
  <section class="publication-year-section" id="year-{{y}}">
    <h2 class="year">{{y}}</h2>
    {% bibliography -f papers -q @*[year={{y}}] %}
  </section>
{% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const yearLinks = document.querySelectorAll('.year-nav a');
  const yearSections = document.querySelectorAll('.publication-year-section');
  const filterButtons = document.querySelectorAll('.publication-filter');
  const publicationEntries = document.querySelectorAll('.publication-entry');
  
  // Set first year as active by default
  if (yearLinks.length) yearLinks[0].classList.add('active');

  function applyFilter(filter) {
    publicationEntries.forEach(entry => {
      const matches = filter === 'all'
        || (filter === 'selected' && entry.dataset.selected === 'true')
        || entry.dataset.category === filter;
      entry.closest('li').hidden = !matches;
    });

    yearSections.forEach(section => {
      const hasVisibleEntries = Array.from(section.querySelectorAll('.publication-entry'))
        .some(entry => !entry.closest('li').hidden);
      section.hidden = !hasVisibleEntries;

      const yearLink = document.querySelector(`.year-nav a[href="#${section.id}"]`);
      if (yearLink) yearLink.hidden = !hasVisibleEntries;
    });

    updateActiveYear();
  }
  
  // Update active state on scroll
  function updateActiveYear() {
    const scrollPosition = window.scrollY;
    const visibleSections = Array.from(yearSections).filter(section => !section.hidden);
    
    visibleSections.forEach((section, index) => {
      const sectionTop = section.offsetTop - 100;
      const nextSection = visibleSections[index + 1];
      const sectionBottom = nextSection
        ? nextSection.offsetTop - 100
        : document.documentElement.scrollHeight;
      
      if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
        yearLinks.forEach(link => link.classList.remove('active'));
        const activeLink = document.querySelector(`.year-nav a[href="#${section.id}"]`);
        if (activeLink) activeLink.classList.add('active');
      }
    });
  }

  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      filterButtons.forEach(item => {
        const isActive = item === button;
        item.classList.toggle('active', isActive);
        item.setAttribute('aria-pressed', isActive);
      });
      applyFilter(button.dataset.filter);
    });
  });
  
  // Update active state on click
  yearLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      yearLinks.forEach(l => l.classList.remove('active'));
      e.target.classList.add('active');
    });
  });
  
  window.addEventListener('scroll', updateActiveYear);
  applyFilter('all');
  updateActiveYear();
});
</script>
