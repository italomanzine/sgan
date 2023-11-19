// static/js/sidebar.js

// Função para alternar o estado do sidebar
function setSidebarState(isMinimized) {
    var sidebar = document.querySelector(".sidebar");
    var centerContent = document.querySelector(".center-content");
    var toggleIcon = document.querySelector(".sidebar-toggle i");

    sidebar.style.width = isMinimized ? "60px" : "250px";
    centerContent.style.marginLeft = isMinimized ? "60px" : "250px";
    toggleIcon.classList.toggle("fa-bars", isMinimized);
    toggleIcon.classList.toggle("fa-arrow-left", !isMinimized);
    sidebar.classList.toggle("minimized", isMinimized);
    sidebar.classList.toggle("active", !isMinimized);
}

// Função para alternar o estado do sidebar
function toggleSidebar() {
    var sidebar = document.querySelector(".sidebar");
    setSidebarState(!sidebar.classList.contains("minimized"));
}

// Função para inicializar o sidebar
function initializeSidebar() {
    setSidebarState(window.innerWidth < 768);
}

// Evento de clique do botão de alternância do sidebar
document.querySelector(".sidebar-toggle").addEventListener("click", toggleSidebar);

// Evento para inicializar o sidebar no carregamento da página
window.addEventListener("load", initializeSidebar);

// Evento para ajustar o sidebar ao redimensionar a janela
window.addEventListener("resize", initializeSidebar);
