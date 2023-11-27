// script.js
document.addEventListener('DOMContentLoaded', function () {
    const wrapper = document.querySelector('.wrapper');
    const sidebarToggle = document.querySelector('.sidebar-toggle');

    sidebarToggle.addEventListener('click', function () {
        wrapper.classList.toggle('sidebar-open');
    });
});