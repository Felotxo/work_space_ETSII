"use strict";

var name = prompt("Introduce nombre", "nombre por defecto");
var age = prompt("¿Qué edad tienes?", 18);
alert("Esto es una alerta, mamones");
var confirmacion = confirm("Estás en una zona excluida de mamones, ¿eres un mamon?");
// Me han dicho que puedo poner comentarios
/* y que además podemos poner comentarios
en varias líneas */
console.log("Esto es un mensaje escrito por consola");
// Al parecer los comentarios no se quedan dentro de las dos barras.
var num = 5;
document.write(num); // valor vale 5
if (true) {
    num = 10;
    document.write(num); // valor vale 10
}
document.write(num);
var num1 = 45;
var num2 = 10; // Añadí esta línea porque num2 no estaba definido
var resultado = num1 + Number(num2);
alert(parseInt(num2) + 23);
const nombre = "FELOTXO";
// JavaScript es Case sensitive.
// Distingue entre mayúsculas/minúsculas
var numero = 10;
var Numero = 20;
console.log("La variable 'numero' vale: " + numero);
console.log("La variable 'Numero' vale: " + Numero);
// Con variables numéricas podemos operar matemáticamente
var sumando1 = 35;
var sumando2 = 45;
var resultadoSuma = sumando1 + sumando2;
console.log("El resultado de sumar " + sumando1 + " + " + sumando2 + " es " + resultadoSuma);
