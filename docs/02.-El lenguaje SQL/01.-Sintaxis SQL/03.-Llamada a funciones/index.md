# 03.-Llamada a funciones
PostgreSQL permite que las funciones que tienen parámetros nombrados se llamen usando notación _posicional_ o _nombrada_. La notación nombrada es especialmente útil para funciones que tienen un gran número de parámetros, ya que hace que las asociaciones entre parámetros y argumentos reales sean más explícitas y fiables. En la notación posicional, una llamada de función se escribe con sus valores argumentales en el mismo orden que se definen en la declaración de función. En la notación, los argumentos se ajustan a los parámetros de la función por su nombre y se pueden escribir en cualquier orden. Para cada notación, también considere el efecto de los tipos de argumentos de función, documentados en [la sección 10](https://www.postgresql.org/docs/current/typeconv-func.html "10.3. Functions").3.

En cualquier notación, los parámetros que tienen valores por defecto dados en la declaración de función no tienen que ser escritos en la llamada en absoluto. Pero esto es particularmente útil en la notación nombrada, ya que cualquier combinación de parámetros puede ser omitida; mientras que en los parámetros de notación posicional sólo se puede omitir de derecha a izquierda.

PostgreSQL también es compatible con notación _mixta_, que combina notación posicional y llamada. En este caso, los parámetros posicionales se escriben primero y aparecen parámetros de nombre después de ellos.

Los siguientes ejemplos ilustrarán el uso de las tres notaciones, utilizando la siguiente definición de función:

CREATE FUNCTION concat.lower-upper(un texto, b texto, mayúscula boolean DEFAULT falso)
Texto de RETURNS
AS
$$
 CASO SELECT
        Cuando $3N UPPER($1 '$ '$ '$ $2)
        ELSE LOWER ($1 " '$ '$ $2)
        END;
$$
LANGUAGE SQL IMMUTABLE STRICT;

Función `concat_lower_or_upper`tiene dos parámetros obligatorios, `a`y `b`. Además hay un parámetro opcional `uppercase`que por defecto a `false`. El `a`y `b`los insumos serán concatenados, y obligados a la parte superior o inferior en función de la `uppercase`parámetro. Los detalles restantes de esta definición de función no son importantes aquí (ver [el capítulo 38](https://www.postgresql.org/docs/current/extend.html "Chapter 38. Extending SQL") para más información).