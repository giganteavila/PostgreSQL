PostgreSQL proporciona un gran número de funciones y operadores para los tipos de  datos incorporados. Este capítulo describe la mayoría de ellos, aunque  en las secciones pertinentes del manual aparecen funciones adicionales  para fines especiales. Los usuarios también pueden definir sus propias  funciones y operadores, como se describe en [la Parte V](https://www.postgresql.org/docs/current/server-programming.html). Los comandos psql  `\df`y  `\do`se puede utilizar para enumerar todas las funciones y operadores disponibles, respectivamente.

La notación utilizada en todo el capítulo para describir los tipos  de argumentos y datos de resultados de una función u operador es así:

```
 repeat( text,  integer) . text
```

que dice que la función  `repeat`toma un texto y un argumento entero y devuelve el resultado de texto tipo.  La flecha derecha también se utiliza para indicar el resultado de un  ejemplo, así:

```
repetición('Pg', 4) PgPgPgPg
```

Si le preocupa la portabilidad, tenga en cuenta que la mayoría de  las funciones y operadores descritos en este capítulo, con la excepción  de los operadores de aritmética y comparación más triviales y algunas  funciones explícitamente marcadas, no se especifican por la  SQLestándar. Parte de esta funcionalidad extendida está presente en otros  SQLsistemas de gestión de bases de datos, y en muchos casos esta funcionalidad es  compatible y coherente entre las diversas implementaciones.