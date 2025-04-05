---
layout: page
title: Postcards
permalink: /photographic_works/postcards/
description: 
nav: false
---

<div class="row mt-3">
  <div class="col-12">
    <h2 class="mb-4">Photography Postcard Collection</h2>
    <div class="project-info mb-4">
      <div class="project-info-item">
        <span class="project-info-label">Author:</span> Zilin Huang
      </div>
      <div class="project-info-item">
        <span class="project-info-label">Created:</span> 2016-2017
      </div>
    </div>
    <p class="mb-5">
      This is a collection of postcards I created from my photography work. Notably, this is the special theme of the 14th “Challenge Cup” China College Student Academic Science and Technology Works Competition. Each image represents a special moment captured through our lens. Enjoy the visual journey!
    </p>
    <div class="acknowledgment mb-5">
      <h5 class="acknowledgment-title"><i class="fas fa-users"></i> Team Acknowledgment</h5>
      <p>
        Special thanks to my team members: <span class="team-member">Junxing Zhang</span>, <span class="team-member">Poyu Zhang</span>, and <span class="team-member">Xiaojian Zheng</span> for their valuable contributions and support.
      </p>
    </div>
  </div>
</div>

<style>
  .project-info {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    padding: 15px;
    background-color: rgba(var(--global-theme-color-rgb), 0.05);
    border-left: 3px solid var(--global-theme-color);
    border-radius: 5px;
    margin-bottom: 25px;
  }
  
  .project-info-item {
    display: flex;
    align-items: center;
  }
  
  .project-info-label {
    font-weight: 600;
    color: var(--global-theme-color);
    margin-right: 8px;
  }
  
  .acknowledgment {
    padding: 15px 20px;
    background-color: rgba(var(--global-theme-color-rgb), 0.03);
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  }
  
  .acknowledgment-title {
    margin-bottom: 10px;
    color: var(--global-theme-color);
    font-size: 1.1rem;
  }
  
  .team-member {
    font-weight: 500;
    background: linear-gradient(120deg, rgba(var(--global-theme-color-rgb), 0.2) 0%, rgba(var(--global-theme-color-rgb), 0.1) 100%);
    padding: 2px 8px;
    border-radius: 4px;
  }
  
  .postcard-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    grid-gap: 20px;
  }
  
  .postcard-item {
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
  }
  
  .postcard-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
  }
  
  .postcard-image {
    width: 100%;
    height: 250px;
    object-fit: cover;
    display: block;
  }
  
  .postcard-caption {
    padding: 10px;
    background: linear-gradient(to top, rgba(0,0,0,0.7), rgba(0,0,0,0));
    color: white;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    opacity: 0;
    transition: opacity 0.3s ease;
  }
  
  .postcard-item:hover .postcard-caption {
    opacity: 1;
  }
  
  @media (max-width: 767px) {
    .postcard-gallery {
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    }
    
    .postcard-image {
      height: 200px;
    }
  }
</style>

<div class="postcard-gallery">
  {% for i in (1..21) %}
    <div class="postcard-item">
      <a href="{{ '/assets/personal/Photography/postcard/' | append: i | append: '.jpg' | relative_url }}" target="_blank">
        <img src="{{ '/assets/personal/Photography/postcard/' | append: i | append: '.jpg' | relative_url }}" 
             alt="Postcard {{ i }}" 
             class="postcard-image"
             loading="lazy">
        <div class="postcard-caption">
          Postcard #{{ i }}
        </div>
      </a>
    </div>
  {% endfor %}
</div>

<div class="row mt-5">
  <div class="col-12">
    <p>
      <a href="{{ '/personal/' | relative_url }}" class="btn btn-sm z-depth-0" role="button">← Back to Personal Page</a>
    </p>
  </div>
</div> 