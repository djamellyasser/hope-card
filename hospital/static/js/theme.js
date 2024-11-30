// Theme toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);

    // Add theme toggle button to navbar
    const navbar = document.querySelector('.navbar-nav:last-child');
    const themeToggle = document.createElement('li');
    themeToggle.className = 'nav-item';
    themeToggle.innerHTML = `
        <button class="nav-link btn btn-link theme-toggle" type="button">
            <i class="fas ${savedTheme === 'dark' ? 'fa-sun' : 'fa-moon'} me-1"></i>
            ${savedTheme === 'dark' ? 'وضع النهار' : 'وضع الليل'}
        </button>
    `;
    navbar.insertBefore(themeToggle, navbar.firstChild);

    // Add click event listener
    const toggleButton = document.querySelector('.theme-toggle');
    toggleButton.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        
        // Update button text and icon
        const icon = toggleButton.querySelector('i');
        icon.className = `fas ${newTheme === 'dark' ? 'fa-sun' : 'fa-moon'} me-1`;
        toggleButton.querySelector('i').nextSibling.textContent = 
            newTheme === 'dark' ? ' وضع النهار' : ' وضع الليل';
    });
});
