// Fetch GitHub stars for repositories
document.addEventListener('DOMContentLoaded', function() {
  // Find all elements with data-github-repo attribute
  const starElements = document.querySelectorAll('.stars[data-github-repo]');
  
  starElements.forEach(function(element) {
    const repo = element.getAttribute('data-github-repo');
    if (repo) {
      // Fetch stars count from GitHub API
      fetch(`https://api.github.com/repos/${repo}`)
        .then(response => response.json())
        .then(data => {
          if (data.stargazers_count !== undefined) {
            element.textContent = data.stargazers_count;
          }
        })
        .catch(error => {
          console.error('Error fetching GitHub stars:', error);
        });
    }
  });
}); 