var numero1 = 10;
var numero2 = 5;
resultado = numero1 / numero2; //resultado = 2
resultado = 3 + numero1; //resultado = 13
resultado = numero2 - 4; //resultado = 1
resultado = numero1 * numero2; //resultado = 50

var precio = 30000;
var dinero = prompt("Introduce cuánto dinero tienes: ");
var edad = prompt("Introduce tu edad:");
if ((precio < dinero) && (edad >=
18)) {
alert("Te puedes comprar el coche");
} else if ((precio < dinero) && (edad
< 18)) {
alert("Tienes el dinero pero nola edad");
}
else if ((precio > dinero) && (edad>= 18))
{alert("Tienes la edad pero no el dinero");
}else if ((precio > dinero) && (edad <
18)) {alert("Ni dinero ni edad");}
for (i=0 ; i<10 ; i++){
    document.write("En esta vuelta de bucle I vale " + i);
    document.write("<br>");
    }
    document.write("Ejecución terminada.");