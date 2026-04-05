function crearEscala(idEscala, idInput, idWrapper) {
    let contenedor = document.getElementById(idEscala);

    for (let i = 1; i <= 10; i++) {
        let btn = document.createElement("button");
        btn.innerHTML = `<span>${i}</span>`;
        btn.type = "button";

        btn.onclick = function () {
            document.getElementById(idInput).value = i;

            let botones = contenedor.querySelectorAll("button");
            botones.forEach(b => b.classList.remove("seleccionado"));
            btn.classList.add("seleccionado");

            let wrapper = document.getElementById(idWrapper);

            if (i <= 8) {
                wrapper.style.display = "block";
                wrapper.querySelector("textarea").required = true;
            } else {
                wrapper.style.display = "none";
                wrapper.querySelector("textarea").required = false;
            }
        };

        contenedor.appendChild(btn);
    }
}

// Validación al enviar
document.querySelector("form").addEventListener("submit", function(e) {
    const val1 = document.getElementById("valor1").value;
    const val2 = document.getElementById("valor2").value;

    if (!val1 || !val2) {
        e.preventDefault();

        if (!val1) resaltarEscala("escala1");
        if (!val2) resaltarEscala("escala2");

        const aviso = document.getElementById("aviso-validacion");
        aviso.style.display = "block";
        setTimeout(() => aviso.style.display = "none", 3500);
    }
});

function resaltarEscala(idEscala) {
    const contenedor = document.getElementById(idEscala);
    contenedor.classList.add("escala-error");
    setTimeout(() => contenedor.classList.remove("escala-error"), 1500);
}

// Botón desactivado hasta responder todo
const btnSubmit = document.querySelector(".btn-submit");
btnSubmit.style.opacity = "0.5";
btnSubmit.style.cursor = "not-allowed";

function verificarBotón() {
    const val1 = document.getElementById("valor1").value;
    const val2 = document.getElementById("valor2").value;

    if (val1 && val2) {
        btnSubmit.style.opacity = "1";
        btnSubmit.style.cursor = "pointer";
    } else {
        btnSubmit.style.opacity = "0.5";
        btnSubmit.style.cursor = "not-allowed";
    }
}

document.getElementById("escala1").addEventListener("click", verificarBotón);
document.getElementById("escala2").addEventListener("click", verificarBotón);

crearEscala("escala1", "valor1", "wrapper-comentario1");
crearEscala("escala2", "valor2", "wrapper-comentario2");

