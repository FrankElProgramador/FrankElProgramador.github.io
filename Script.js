// Seleccionar un elemento
//let boton = document.getElementById("MiBoton");
//let elemento = document.getElementById("miElemento");  // Selecciona por ID
//let parrafo = document.querySelector("p");  // Selecciona el primer <p>
//let elementos = document.getElementsByClassName("clase");  // Selecciona todos los elementos con la clase
//let tecla = document.addEventListener("keydown", function(evento) {console.log("Tecla presionada: " + evento.key);});
//let formulario = document.getElementById("miFormulario");
//let traerAyardo = document.getElementById("yardo");
// Usando var
var nombre = "Ana";
// Usando let
let edad = 25;

// Usando const
const PI = 3.1416;
let caja = document.getElementById("miCaja");
let caja2 = document.getElementById("miCaja2");
let boton2 = document.getElementById("boton2");
let boton3 = document.getElementById("boton3");
let boton4 = document.getElementById("boton4");

caja2.style.display = "none";
function Agregar(){
// Agregar una clase
caja.classList.add("highlight");
caja2.classList.add("highlight");
}
function Quitar(){
    // Eliminar una clase
caja.classList.remove("highlight");
caja2.classList.remove("highlight");
}

boton2.addEventListener("click", Quitar);
boton3.addEventListener("click", function(){// Alternar una clase (si está, la quita; si no está, la añade)
    caja.classList.toggle("highlight");caja2.classList.toggle("highlight");});

function Ocultar(){
    
    if (caja.style.display === "none") {
        caja.style.display = "block";
    }
    else {
        caja.style.display = "none";
    }

    if (caja2.style.display === "none") {
        caja2.style.display = "block";
    }
    else {
        caja2.style.display = "none";
    }
    /*caja.style.display = "none";
    caja2.style.display = "block";

    caja.style.display = "block";
    caja2.style.display = "none";
    */
    };

// Agregar un evento de clics


/*
caja.addEventListener("mouseout", function() {
    caja.style.backgroundColor = "white";
    caja.style.fontSize = "20px";
    caja.style.color = "black";
});


formulario.addEventListener("submit", function(evento) {
    evento.preventDefault();  // Evita que el formulario se envíe
    alert("Formulario enviado");
});

console.log(addEventListener)

function convertirAEnterto(numero) {
    numero = 78.9;
    alert("El número convertido es: " + numero);
    return parseInt(numero);
}

traerAyardo.addEventListener("click", convertirAEnterto);

    
// Cambiar el color de fondo
caja.style.backgroundColor = "lightblue";

// Cambiar el tamaño de la fuente
caja.style.fontSize = "20px";

// Ocultar el elemento
caja.style.display = "none";

// Mostrar el elemento
caja.style.display = "block";

// Agregar evento para cambiar estilos al hacer clic
boton.addEventListener("click", function() {
    caja.classList.toggle("highlight");  // Alterna la clase 'highlight'
    caja.style.backgroundColor = "lightgreen";  // Cambia el color de fondo
});



*/






