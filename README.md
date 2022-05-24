# Buscaminas
El clásico Juego de buscaminas para que te diviertas jugandolo.<br>
<h2>Autor</h2>
Nikolas Zúñiga 
</u1>
<h2>¿Que se utilizó?</h2>
Para que el código funcione se utilizó varias funciones, encargadas de generar el campo, generar las minas, etc. Dentro se uso distintos elementos como listas anidadas, bucles for y while, y condicionales.<br>
<h2>¿Cómo usar?</h2>
Al iniciar, se genera un campo de 10x10 casillas, con 10 minas en lugares aleatorios. El jugador tendrá que ingresar las coordenadas de la casilla que quiere minar, si la casilla elegida no es una mina, obtendrá un número el cual es la cantidad de minas que hay alrededor de esa casilla, de esa forma el jugador tendrá que minar todas las casillas excepto las 10 minas para poder ganar.
<h2>Ejemplo:</h2>
---------------------------------------------<br>
 _ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |  <br>
---------------------------------------------<br>
0 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
1 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
2 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
3 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
4 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
5 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
6 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
7 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
8 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
9 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
---------------------------------------------<br>
Escoge las coordenadas de la casilla que quieres minar (Ejemplo: 5 5): 5 5<br>
---------------------------------------------<br>
 _ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |  <br>
---------------------------------------------<br>
0 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
1 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
2 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
3 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
4 | _ | _ | _ | _ | 0 | 0 | 1 | _ | _ | _ |<br>
5 | _ | _ | _ | _ | 0 | 0 | 0 | _ | _ | _ |<br>
6 | _ | _ | _ | _ | 0 | 0 | 0 | _ | _ | _ |<br>
7 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
8 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
9 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
---------------------------------------------<br>
Escoge las coordenadas de la casilla que quieres minar (Ejemplo: 5 5): 3 7<br>
 _ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |  <br>
---------------------------------------------<br>
0 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
1 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
2 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
3 | _ | _ | _ | _ | _ | _ | _ | X | _ | _ |<br>
4 | _ | _ | _ | _ | 0 | 0 | 1 | _ | _ | _ |<br>
5 | _ | _ | _ | _ | 0 | 0 | 0 | _ | _ | _ |<br>
6 | _ | _ | _ | _ | 0 | 0 | 0 | _ | _ | _ |<br>
7 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
8 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
9 | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ |<br>
---------------------------------------------<br>
Ups, minaste una mina. El juego termino.!!!!!
