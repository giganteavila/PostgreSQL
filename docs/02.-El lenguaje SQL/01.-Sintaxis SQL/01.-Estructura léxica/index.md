La entrada SQL consiste en una secuencia de *comandos*. Un comando se compone de una secuencia de *tokens*, terminada por un puntomico (   . El final de la corriente de entrada también termina un comando. Qué  fichas son válidas depende de la sintaxis del comando en particular.

Un token puede ser una *palabra clave*, un *identificador*, un *identificador cotizado*, un *literal* (o constante), o un símbolo de caracteres especial. Los fichas  normalmente se separan por espacio en blanco (espacio, pestaña,  newline), pero no tienen por qué ser si no hay ambiguedad (que  generalmente es sólo el caso si un carácter especial está adyacente a  algún otro tipo simbólico).

Por ejemplo, lo siguiente es (syntácticamente) la entrada SQL válida:

```
SELECT * DESDE MITABLE;
Actualización MY-TABLE SET A = 5;
INSERT INTO MALL VALUE (3, 'hola allí');
```

Esta es una secuencia de tres comandos, uno por línea (aunque esto  no se requiere; más de un comando puede estar en una línea, y los  comandos pueden ser divididos útilmente a través de las líneas).

Además, *los comentarios* pueden ocurrir en la entrada de SQL. No son fichas, son efectivamente equivalentes al espacio en blanco.

La sintaxis SQL no es muy consistente con respecto a qué fichas  identifican los comandos y cuáles son operandos o parámetros. Las  primeras fichas son generalmente el nombre de comando, así que en el  ejemplo anterior normalmente hablaríamos de un "SELECT", un "ActADE", y un INSERTcomando INSERT. Pero, por ejemplo, el  `UPDATE`El mando siempre requiere un  `SET`token aparecer en una determinada posición, y esta variación particular de  `INSERT`también requiere un  `VALUES`para estar completa. Las reglas de sintaxis precisas para cada comando se describen en [la Parte VI](https://www.postgresql.org/docs/current/reference.html).

