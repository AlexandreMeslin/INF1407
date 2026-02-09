onload = () => {
    // Código para o modal
    const modal = document.getElementById("modal");
    const btnAbrir = document.getElementById("btnAbrir");
    const btnFechar = document.getElementById("btnFechar");

    // Abrir modal
    btnAbrir.onclick = () => {
        modal.style.display = "flex";
    };

    // Fechar modal
    btnFechar.onclick = () => {
        modal.style.display = "none";
    };

    // Fechar clicando fora da caixa
    modal.onclick = (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };
};

