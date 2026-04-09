addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("id_password");
    const msg = document.getElementById("mensagem");

    input.addEventListener("keydown", function (e) {
        const caps = e.getModifierState && e.getModifierState("CapsLock");

        // Detecta CapsLock ativo
        if (caps) {
            msg.style.display = "block";
            msg.textContent = "Aviso: CapsLock está ativado!";
        } else {
            msg.style.display = "none";
            msg.textContent = "";
        }
    });
});




