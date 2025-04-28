let botonEnviar = document.getElementById("BtnEnviar");
let caja2 = document.getElementById("miCaja2");
caja2.style.display = "none";
function enviarDatos() {
    alert("¡Gracias por suscribirte!");
}

function mostrarMenu(){
    let menu = document.getElementById("miCaja2");
    if (menu.style.display === "none") {
        setTimeout(() => {
            menu.style.display = 'block';
          }, 500); // Retraso de 500 milisegundos
        menu.style.transition = "all 20s ease"; // Transición suave para el menú
        menu.style.opacity = "20"; // Opacidad del menú
        menu.style.transform = "translateY(0)"; // Efecto de desplazamiento al mostrar el menú
        menu.style.animation = "fadeIn 5s"; // Animación de aparición
        menu.style.animationFillMode = "forwards"; // Mantener el estado final de la animación
        menu.style.animationTimingFunction = "ease-in-out"; // Función de temporización para la animación
        menu.style.animationDelay = "3s"; // Retraso de la animación
    } else {
        menu.style.display = "none";
    }
}