// static/js/sidebar.js
// Quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function() {
    var sidebar = document.querySelector('.sidebar');
    var toggleButton = document.querySelector('.sidebar-toggle');

    toggleButton.addEventListener('click', function() {
        // Adiciona ou remove a classe 'active' do sidebar
        sidebar.classList.toggle('active');
        // Altera o ícone do botão de acordo com o estado do sidebar
        if (sidebar.classList.contains('active')) {
            toggleButton.textContent = ''; // Limpa o texto do botão
            toggleButton.classList.add('active'); // Adiciona classe 'active' para o botão
        } else {
            toggleButton.textContent = '☰ Menu'; // Texto original do botão
            toggleButton.classList.remove('active'); // Remove classe 'active' do botão
        }
    });
});
  