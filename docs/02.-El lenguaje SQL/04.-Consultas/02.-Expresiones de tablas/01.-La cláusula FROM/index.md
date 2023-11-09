El  [`FROM`](https://www.postgresql.org/docs/current/sql-select.html#SQL-FROM)la cláusula deriva un cuadro de uno o más cuadros que figuran en una lista de referencia de la tabla separada por comas.

```
De los DE  table_reference[,  table_reference[, ...]]
```

Una referencia de tabla puede ser un nombre de tabla  (posiblemente calificado de esquema), o una tabla derivada, como una  subcoquería, a  `JOIN`construir, o combinaciones complejas de estos. Si se enumera más de una referencia de cuadro en la  `FROM`cláusula, las tablas se entrenan (es decir, se forma el producto cartesiano de sus filas; véase más abajo). El resultado de la  `FROM`lista es una tabla virtual intermedia que puede estar sujeta a transformaciones por la `WHERE`, `GROUP BY`, y  `HAVING`cláusulas y es finalmente el resultado de la expresión general de la tabla.



Cuando una tabla de referencia nombra una tabla que es la madre  de una jerarquía de herencia de tabla, la referencia de la tabla produce filas no sólo de esa tabla sino de todas sus tablas descendientes, a  menos que la palabra clave  `ONLY`precede al nombre de la tabla. Sin embargo, la referencia produce sólo las  columnas que aparecen en la tabla nombrada, se ignoran las columnas  añadientes en subtables.

En vez de escribir  `ONLY`antes del nombre de la mesa, puede escribir  `*`después del nombre de la tabla para especificar explícitamente que se incluyen  las tablas descendientes. Ya no hay ninguna razón real para usar esta  sintaxis, porque buscar tablas de descendientes es ahora siempre el  comportamiento predeterminado. Sin embargo, se apoya para la  compatibilidad con versiones más antiguas.