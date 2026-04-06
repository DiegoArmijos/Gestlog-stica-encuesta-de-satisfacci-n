document.addEventListener("DOMContentLoaded", function () {

    // ── Crear escalas ──
    crearEscala("escala1", "valor1", "wrapper-comentario1");
    crearEscala("escala2", "valor2", "wrapper-comentario2");

    // ── Botón enviar desactivado hasta responder todo ──
    const btnSubmit = document.querySelector(".btn-submit");
    btnSubmit.style.opacity = "0.5";
    btnSubmit.style.cursor  = "not-allowed";

// Reemplaza la función verificarBoton existente con esta:
    function verificarBoton() {
        const val1   = document.getElementById("valor1").value;
        const val2   = document.getElementById("valor2").value;
        const nombre = document.getElementById("nombre").value.trim();
        const listo  = val1 && val2 && nombre;
        btnSubmit.style.opacity = listo ? "1"       : "0.5";
        btnSubmit.style.cursor  = listo ? "pointer" : "not-allowed";
    }

// Agrega este listener después de donde creas las escalas:
document.getElementById("nombre").addEventListener("input", verificarBoton);

    // ── Validación al enviar ──
    document.querySelector("form").addEventListener("submit", function (e) {
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

    function crearEscala(idEscala, idInput, idWrapper) {
        const contenedor = document.getElementById(idEscala);
        if (!contenedor) return;

        for (let i = 1; i <= 5; i++) {
            const btn = document.createElement("button");
            btn.type = "button";
            btn.innerHTML = "<span>" + i + "</span>";

            btn.addEventListener("click", function () {
                document.getElementById(idInput).value = i;

                contenedor.querySelectorAll("button")
                          .forEach(function(b) { b.classList.remove("seleccionado"); });
                btn.classList.add("seleccionado");

                const wrapper = document.getElementById(idWrapper);
                const textarea = wrapper.querySelector("textarea");

                if (i <= 3) {
                    wrapper.style.display = "block";
                    textarea.required = true;
                } else {
                    wrapper.style.display = "none";
                    textarea.required = false;
                    textarea.value = "";
                }

                verificarBoton();
            });

            contenedor.appendChild(btn);
        }
    }

});