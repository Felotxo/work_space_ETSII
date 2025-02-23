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
var precio=30000;
var dinero=prompt("Introduce cuantodinero tienes: ");
if(dinero>precio){
alert("Te puedes comprar elcoche");
}else{
alert("Te vas en autobus");
}
var array1=["objeto1","objeto2","objeto3"];
array1[3]="objeto4";
array1[4]=prompt("Introduce objeto4");
alert(array1[4]);
