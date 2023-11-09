[El cuadro 9.16](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-TABLE) enumera los operadores disponibles para la coincidencia de patrones utilizando expresiones regulares POSIX.

**Cuadro 9.16. Operadores de partido de expresión regular**

| Operadora                Descripción                Ejemplos (s) |
| ------------------------------------------------------------ |
| `text``~``text`- `boolean`                La cuerda coincide con la expresión regular, caso sensiblemente                 `'thomas' ~ 't.*ma'`- |
| `text``~*``text`- `boolean`                La cuerda coincide con la expresión regular, caso insensiblemente                 `'thomas' ~* 'T.*ma'`- |
| `text``!~``text`- `boolean`                Cada no coincide con la expresión regular, caso sensiblemente                 `'thomas' !~ 't.*max'`- |
| `text``!~*``text`- `boolean`                Cada no coincide con la expresión regular, insensiblemente                 `'thomas' !~* 'T.*ma'`- |

 POSIXlas expresiones regulares proporcionan un medio más potente para la combinación de patrones que el  `LIKE`y  `SIMILAR TO`operadores. Muchas herramientas Unix como `egrep`, `sed`, o  `awk`utilizar un lenguaje que coinija un patrón que sea similar al descrito aquí.

Una expresión regular es una secuencia de caracteres que es una definición abreviada de un conjunto de cuerdas (un *conjunto regular*). Se dice que una cadena coincide con una expresión regular si es un  miembro del conjunto regular descrito por la expresión regular. Al igual que con `LIKE`, los caracteres de patrón coinciden exactamente con caracteres de cadena a menos que sean caracteres especiales en el lenguaje de expresión  regular, pero las expresiones regulares utilizan diferentes caracteres  especiales que  `LIKE`- Sí. A diferencia de  `LIKE`patrones, una expresión regular se permite que coinzca en cualquier lugar dentro  de una cadena, a menos que la expresión regular esté explícitamente  anclada al principio o al final de la cuerda.

Algunos ejemplos:

```
'abcd' - 'bc' verdad
'abcd' "a.c" true "-" punto coincide con cualquier personaje
"abcd" "a".  *repite el elemento de patrón anterior
"abcd" """ verdad "  |OR, grupo de paréntesis
'abcd' - "A" verdad  ^Ancla para empezar la cuerda
"abcd" "" "" falso" coincidiría excepto por anclaje
```

El  POSIXEl lenguaje patrón se describe con mucho mayor detalle a continuación.

El  `substring`función con dos parámetros, `substring(*`string`* from *`pattern`*)`, proporciona la extracción de una subcadeing que coincide con un patrón  de expresión regular POSIX. Devuelve nula si no hay coincidencia, de lo  contrario la primera parte del texto que coinía con el patrón. Pero si  el patrón contiene algún paréntesis, la parte del texto que coinía con  la primera subexpresión entre paréntesis (la que entre paréntesis deja  primero) es devuelta. Puede poner paréntesis alrededor de toda la  expresión si desea usar paréntesis dentro de ella sin desencadenar esta  excepción. Si necesita paréntesis en el patrón antes de la subexpresión  que desea extraer, consulte los paréntesis no de captura descritos a  continuación.

Algunos ejemplos:

```
substring('foobar' de 'o.b') oob
substring ('foobar' de 'o(.)b') o
```

El  `regexp_count`función cuenta el número de lugares donde un patrón de expresión regular POSIX coincide con una cadena. Tiene la sintaxis `regexp_count`(*`string`*,  *`pattern`*[,  *`start`*[,  *`flags`*]]].  *`pattern`*se busca en *`string`*, normalmente desde el principio de la cuerda, pero si el  *`start`*El parámetro se proporciona entonces a partir de ese índice de caracteres. El  *`flags`*El parámetro es una cadena de texto opcional que contiene cero o más  banderas de letras simples que cambian el comportamiento de la función.  Por ejemplo, incluyendo  `i`en  *`flags`*especifica la correspondencia insensible a los casos. Las banderas apoyadas se describen en el .

Algunos ejemplos:

```
reexpádolos ('ABCABCAXYaxy', 'A.')          3
reexpádoto ('ABCABCAXYaxy', 'A.', 1, 'i') 4
```

El  `regexp_instr`función devuelve la posición de partida o final de la *`N`*'th match de un patrón de expresión regular POSIX a una cadena, o cero si no hay tal coincidencia. Tiene la sintaxis `regexp_instr`(*`string`*,  *`pattern`*[,  *`start`*[,  *`N`*[,  *`endoption`*[,  *`flags`*[,  *`subexpr`*]]]]]]].).  *`pattern`*se busca en *`string`*, normalmente desde el principio de la cuerda, pero si el  *`start`*El parámetro se proporciona entonces a partir de ese índice de caracteres. Si  *`N`*se especifica entonces la *`N`*La coincidencia del patrón se encuentra, de lo contrario el primer partido se encuentra. Si el  *`endoption`*El parámetro se omite o se especifica como cero, la función devuelve la  posición del primer carácter del partido. De lo contrario,  *`endoption`*debe ser una, y la función devuelve la posición del personaje después del partido. El  *`flags`*El parámetro es una cadena de texto opcional que contiene cero o más  banderas de letras simples que cambian el comportamiento de la función.  Las banderas apoyadas se describen en el . Para un patrón que contenga subexpresiones entre paréntesis,  *`subexpr`*es un entero que indica qué subexpresión es de interés: el resultado  identifica la posición de la subcadenación que coincide con esa  subexpresión. Las subexpresiones están numeradas en el orden de sus  principales paréntesis. Cuando  *`subexpr`*se omite o cero, el resultado identifica la posición de todo el partido  independientemente de las subexpresiones entre paréntesis.

Algunos ejemplos:

```
reexp-instr ('número de tu calle, cremallera de la ciudad, FR', ',]', 1, 2)
                                   23
regexp-instr ('ABCDEFGHI', '(c...o.o.', 1, 1, 0, 'i', 2)
                                   6
```

El  `regexp_like`función comprueba si la coincidencia de un patrón de expresión regular de POSIX ocurre dentro de una cadena, devolviendo booleano true o falso. Tiene  la sintaxis `regexp_like`(*`string`*,  *`pattern`*[,  *`flags`*] ]). El  *`flags`*El parámetro es una cadena de texto opcional que contiene cero o más  banderas de letras simples que cambian el comportamiento de la función.  Las banderas apoyadas se describen en el . Esta función tiene los mismos resultados que la  `~`operador si no se especifican banderas. Si tan solo la  `i`la bandera se especifica, tiene los mismos resultados que la  `~*`operador.

Algunos ejemplos:

```
regexp-like('Hello Mundo', 'mundo') falso
reexp-like('Hello Mundo', 'mundo', 'i') cierto
```

El  `regexp_match`función devuelve un array de texto de subcadeing (s) a juego dentro de la  primera coincidencia de un patrón de expresión regular POSIX a una  cadena. Tiene la sintaxis `regexp_match`(*`string`*,  *`pattern`*[,  *`flags`*] ]). Si no hay coincidencia, el resultado es `NULL`. Si se encuentra una coincidencia, y la  *`pattern`*no contiene subexpresiones entre paréntesis, luego el resultado es un  array de texto de un solo elemento que contiene la subcadenación que  coincide con todo el patrón. Si se encuentra una coincidencia, y la  *`pattern`*contiene subexpresiones entre paréntesis, entonces el resultado es un conjunto de texto que *`n`*El elemento es la subcarra que se corresponde con el *`n`*Supresión entre paréntesis de la  *`pattern`*(sin contar - no capturar paréntesis; ver abajo para más detalles). El  *`flags`*El parámetro es una cadena de texto opcional que contiene cero o más  banderas de letras simples que cambian el comportamiento de la función.  Las banderas apoyadas se describen en el .

Algunos ejemplos:

```
SELECT regexp-match('foobarbequebaz', 'bar.*que');
 regexp-match
--------------
 Bárbaraca.
(1 fila)

SELECT regexp-match('foobarbequebaz', '(bar)(beque)');
 regexp-match
--------------
 Bar, aque.
(1 fila)
```

### Tip

En el caso común en el que sólo quieres toda la substring o  `NULL`para no coincidir, la mejor solución es usar `regexp_substr()`. Sin embargo,  `regexp_substr()`solo existe en PostgreSQL versión 15 y más. Cuando se trabaja en versiones anteriores, puede extraer el primer elemento de `regexp_match()`Resultado, por ejemplo:

```
SELECT (regexp-match('foobarbequebaz', 'bar.*que'))[1];
 regexp-match
--------------
 barbacoa
(1 fila)
```

El  `regexp_matches`función devuelve un conjunto de conjuntos de texto de subcadeings de  coincidencias dentro de los partidos de un patrón de expresión regular  POSIX a una cadena. Tiene la misma sintaxis que `regexp_match`. Esta función no devuelve filas si no hay partido, una fila si hay un partido y el  `g`la bandera no se da, o  *`N`*filas si las hay  *`N`*cerdos y la  `g`La bandera se da. Cada fila devuelta es un array de texto que contiene  toda la subcadenación empareja o las sub-cuerdas que coinciden con  subexpresiones entre paréntesis de la *`pattern`*, tal como se describe anteriormente para `regexp_match`.  `regexp_matches`acepta todas las banderas que aparecen en la , más  `g`bandera que le ordena devolver todos los partidos, no solo el primero.

Algunos ejemplos:

```
SELECT regexp-matches ('foo', 'no allí');
 regexp-matches
----------------
(0 filas)

SELECT regexp-matches ('foobarbequebazilbarfbonk', '(b[-b])(b[-b])', 'g');
 regexp-matches
----------------
 Bar, aque.
 Barzil, Barf.
(2 filas)
```

### Tip

En la mayoría de los casos  `regexp_matches()`debe utilizarse con la  `g`bandera, ya que si solo quieres el primer partido, es más fácil y más eficiente de usar `regexp_match()`. Sin embargo,  `regexp_match()`solo existe en PostgreSQL versión 10 y up. Cuando se trabaja en versiones anteriores, un truco común es colocar un  `regexp_matches()`llamada en una subseleccione, por ejemplo:

```
SELECT col1, (SELECT regexp-matches(col2, '(bar)(beque))) De la pestaña;
```

Esto produce una matriz de texto si hay una coincidencia, o  `NULL`si no, lo mismo que  `regexp_match()`lo haría. Sin la subseleccionada, esta consulta no produciría ninguna  salida para las filas de mesa sin una coincidencia, que normalmente no  es el comportamiento deseado.

El  `regexp_replace`función proporciona sustitución de nuevo texto por subcadenas que coincidan con los patrones de expresión regulares de POSIX. Tiene la sintaxis `regexp_replace`(*`source`*, *`pattern`*,  *`replacement`*[,  *`start`*[,  *`N`*]] [,  *`flags`*] ]). (Aviso que  *`N`*no puede especificarse a menos que  *`start`*es, pero  *`flags`*puede darse en cualquier caso.) El  *`source`*cuerda se devuelve sin cambios si no hay coincidencia con el *`pattern`*. Si hay una coincidencia, la  *`source`*cuerda se devuelve con el  *`replacement`*cuerda sustituida por la subcadería a juego. El  *`replacement`*cuerdas pueden contener `\`*`n`*, dónde  *`n`*es de 1 a 9, para indicar que la substring fuente que coincida con la *`n`*'se debe insertar la subexpresión entre paréntesis del patrón, y puede contener  `\&`indicar que se debe insertar la subcadena que coincida con todo el patrón. Escribir  `\\`si necesita poner una reacción literal en el texto de reemplazo.  *`pattern`*se busca en *`string`*, normalmente desde el principio de la cuerda, pero si el  *`start`*El parámetro se proporciona entonces a partir de ese índice de caracteres. Por defecto, sólo se reemplaza el primer partido del patrón. Si  *`N`*se especifica y es mayor que cero, luego el *`N`*'La coincidencia del patrón se reemplaza. Si el  `g`se da bandera, o si  *`N`*se especifica y es cero, luego todos los partidos en o después de la  *`start`*se sustituye la posición. (El  `g`bandera es ignorada cuando  *`N`*se especifica.) El  *`flags`*El parámetro es una cadena de texto opcional que contiene cero o más  banderas de letras simples que cambian el comportamiento de la función.  Bandas apoyadas (aunque no `g`) se describen en el [cuadro 9.24](https://www.postgresql.org/docs/current/functions-matching.html#POSIX-EMBEDDED-OPTIONS-TABLE).

Algunos ejemplos:

```
reexp-replace( 'foobarbaz', 'b.', 'X')
                                   fooXbaz
regex-replace( 'foobarbaz', 'b.', 'X', 'g')
                                   fooXX
reexp-replace( 'foobarbaz', 'b(...', 'X-1Y', 'g')
                                   fooXarYXazY
reexp-replace('A PostgreSQL function', 'a-e-i-o'u', 'X', 1, 0, 'i')
                                   X PXstgrXSQL fXnctXXn
reexp-replace('A PostgreSQL function', 'a-e-i-o'u', 'X', 1, 3, 'i')
                                   Una función de PostgrXSQL
```

El  `regexp_split_to_table`función divide una cadena usando un patrón de expresión regular POSIX como delimitador. Tiene la sintaxis `regexp_split_to_table`(*`string`*,  *`pattern`*[,  *`flags`*] ]). Si no hay coincidencia con el *`pattern`*, la función devuelve el *`string`*. Si hay al menos un partido, para cada partido devuelve el texto desde  el final del último partido (o el comienzo de la cuerda) hasta el  comienzo del partido. Cuando no hay más partidos, devuelve el texto  desde el final del último partido hasta el final de la cuerda. El  *`flags`*El parámetro es una cadena de texto opcional que contiene cero o más  banderas de letras simples que cambian el comportamiento de la función.  `regexp_split_to_table`soporta las banderas descritas en la [Tabla 9.24](https://www.postgresql.org/docs/current/functions-matching.html#POSIX-EMBEDDED-OPTIONS-TABLE).

El  `regexp_split_to_array`función se comporta igual que `regexp_split_to_table`, excepto que  `regexp_split_to_array`devuelve su resultado como una serie de `text`. Tiene la sintaxis `regexp_split_to_array`(*`string`*,  *`pattern`*[,  *`flags`*] ]). Los parámetros son los mismos que para `regexp_split_to_table`.

Algunos ejemplos:

```
SELECT foo De regexp-split-to-table (el zozoxo marrón rápido salta sobre el perro perezoso", 's') AS foo;
  foo
------
 el
 rápido
 marrón
 zozorón
 saltos
 sobre
 el
 perezoso
 perro
(9 filas)

SELECT regexp.split-to-array ('el zozorón marrón rápido salta sobre el perro perezoso', 's');
              regexp.split-to-array
-------------------------------------------------------------
 - El,quick,brown,fox,jumps,over, el,elzy, perroja.
(1 fila)

SELECT foo FROM regexp.split-to-table ('el zozoco marrón rápido', 's*') AS foo;
 foo
-----
 t
 h
 e
 q
 u
 - I
 c
 k
 b
 r
 o
 w
 n
 f
 o
 x
(16 filas)
```

Como demuestra el último ejemplo, las funciones de división de  regexp ignoran los partidos de longitud cero que ocurren al principio o  al final de la cuerda o inmediatamente después de un partido anterior.  Esto es contrario a la definición estricta de la correspondencia de  regexp que es implementada por las otras funciones de regexp, pero  generalmente es el comportamiento más conveniente en la práctica. Otros  sistemas de software como Perl utilizan definiciones similares.

El  `regexp_substr`función devuelve la substring que coincide con un patrón de expresión regular POSIX, o  `NULL`si no hay coincidencia. Tiene la sintaxis `regexp_substr`(*`string`*,  *`pattern`*[,  *`start`*[,  *`N`*[,  *`flags`*[,  *`subexpr`*]]]]].).  *`pattern`*se busca en *`string`*, normalmente desde el principio de la cuerda, pero si el  *`start`*El parámetro se proporciona entonces a partir de ese índice de caracteres. Si  *`N`*se especifica entonces la *`N`*El partido del patrón se devuelve, de lo contrario se devuelve el primer partido. El  *`flags`*El parámetro es una cadena de texto opcional que contiene cero o más  banderas de letras simples que cambian el comportamiento de la función.  Las banderas apoyadas se describen en el . Para un patrón que contenga subexpresiones entre paréntesis,  *`subexpr`*es un entero que indica qué subexpresión es de interés: el resultado es la subcadenación que coincide con esa subexpresión. Las subexpresiones  están numeradas en el orden de sus principales paréntesis. Cuando  *`subexpr`*se omite o cero, el resultado es todo el partido independientemente de las subexpresiones entre paréntesis.

Algunos ejemplos:

```
reexp-substr( 'número de tu calle, cremallera de la ciudad, FR', ',', 1, 2)
                                    la ciudad cremallera
regexp-substr('ABCDEFGHI', '(c...'.', 1, 1, 'i', 2)
                                   FGH
```