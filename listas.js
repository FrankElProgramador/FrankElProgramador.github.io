/*const entrada = document.getElementById("entrada");
result = document.getElementById("resultado");
const boton = document.getElementById("boton");
function ejecutar(){let edad = parseInt(entrada.value);console.log(edad);if (edad < 18 && edad >= 1) {result.innerHTML = "Eres menor de edad, tienes: " + edad + " años";}else if (edad >= 18 && edad < 60) {result.innerHTML = "Eres mayor de edad, tienes " + edad + " años";} else if (edad >= 60 && edad <= 100) {result.innerHTML = "Eres adulto mayor " + edad + " años";} else {result.innerHTML = "Edad no válida :" + edad;}};
*/

num1 = document.getElementById("entrada1");
num2 = document.getElementById("entrada2");
result = document.getElementById("resultado");
const boton = document.getElementById("boton1");

function ejecutarsuma() {
    num1 = parseInt(num1.value);
    num2 = parseInt(num2.value);
    for (i = 0; i < 13; i++) {
        if (isNaN(num1) || isNaN(num2)) {
            result.innerHTML = "No es un número válido";
            break;
        }
        else if (num1 < 0 || num2 < 0) {
            result.innerHTML = "No es un número válido";
            break;
        } else {
            result.innerHTML = "La suma es: " + (num1 + num2);
            result.innerHTML += "<br> La resta es: " + (num1 - num2);
            result.innerHTML += "<br> La multiplicación es: " + (num1 * num2);
            result.innerHTML += "<br> La división es: " + (num1 / num2);
            result.innerHTML += "<br> El módulo es: " + (num1 % num2);
            result.innerHTML += "<br> La potencia es: " + (num1 ** num2);
            result.innerHTML += "<br> La raíz cuadrada de " + num1 + " es: " + Math.sqrt(num1);
            break;
        }
    }
}
//result.innerHTML = "Eres menor de edad, tienes: " + edad + " años <br>";
class Persona {
    constructor(nombre, edad, ocupacion) {
        this.nombre = nombre;
        this.edad = edad;
        this.ocupacion = ocupacion;
    }
    saludar() {
        return "Hola, mi nombre es " + this.nombre + " y tengo " + this.edad + " años.";
    }
    decirOcupacion() {
        return "Soy " + this.ocupacion;
    }
}
const persona = new Persona("Yardo",22,"Chatarrero");
console.log(persona.saludar());