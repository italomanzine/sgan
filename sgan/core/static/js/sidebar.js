// static/js/sidebar.js

// Função para alternar o estado do sidebar e ajustar o header
function setSidebarState(isMinimized) {
    var sidebar = document.querySelector(".sidebar");
    var centerContent = document.querySelector(".center-content");
    var header = document.querySelector("header"); // Adiciona uma referência ao header
    var toggleIcon = document.querySelector(".sidebar-toggle i");

    // Ajusta o width do sidebar e a margem esquerda do conteúdo principal e do header
    sidebar.style.width = isMinimized ? "60px" : "250px";
    centerContent.style.marginLeft = isMinimized ? "60px" : "250px";
    header.style.left = isMinimized ? "60px" : "250px"; // Ajusta o left do header

    // Alterna as classes para ícones de minimizar e maximizar
    toggleIcon.classList.toggle("fa-bars", isMinimized);
    toggleIcon.classList.toggle("fa-arrow-left", !isMinimized);
    
    // Alterna as classes para o estado minimizado e ativo do sidebar
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
window.addEventListener("resize", function() {
    initializeSidebar();
});
