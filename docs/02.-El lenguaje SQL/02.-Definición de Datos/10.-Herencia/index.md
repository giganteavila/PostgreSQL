PostgreSQL implementa la herencia de tabla, que puede ser una herramienta útil  para los diseñadores de bases de datos. (SQL:1999 y más tarde definir  una característica de herencia de tipo, que difiere en muchos aspectos  de las características descritas aquí.)

Empecemos por un ejemplo: supongamos que estamos tratando de  construir un modelo de datos para las ciudades. Cada estado tiene muchas ciudades, pero sólo una capital. Queremos poder recuperar rápidamente  la capital para cualquier estado en particular. Esto se puede hacer  creando dos mesas, una para las capitales de los estados y otra para las ciudades que no son capitales. Sin embargo, qué pasa cuando queremos  pedir datos sobre una ciudad, independientemente de si es una capital o  no? La característica de herencia puede ayudar a resolver este problema. Definimos el  `capitals`mesa para que herede de `cities`:

```
CREATE TABLE ciudades (CádCR)
    texto de nombre,
    flotar población,
    elevación en los pies - en los pies
);

Capitales de la TABLA (CádCR)
    estado char (2)
) INHERITS (ciudades);
```

En este caso, el  `capitals`la tabla *hereda* todas las columnas de su tabla matriz, `cities`. Las capitales del Estado también tienen una columna adicional, `state`, eso muestra su estado.

En PostgreSQL, una tabla puede heredar de cero o más otras tablas, y una consulta  puede hacer referencia a todas las filas de una tabla o a todas las  filas de una tabla más todas sus tablas descendientes. Este último  comportamiento es el predeterminado. Por ejemplo, la siguiente consulta  encuentra los nombres de todas las ciudades, incluidas las capitales de  los estados, que se encuentran en una elevación de más de 500 pies:

```
Nombre SELECT, elevación
    De las ciudades
    La elevación de Dónde sectura 500;
```

Dados los datos de la muestra del tutorial PostgreSQL (ver [Sección 2.1](https://www.postgresql.org/docs/current/tutorial-sql-intro.html)), esto devuelve:

```
nombre de la elevación
---------------------
 Las Vegas 2174
 Mariposa - 1953
 Madison 845
```

Por otro lado, la siguiente consulta encuentra todas las ciudades  que no son capitales de estado y están situadas en una elevación de más  de 500 pies:

```
Nombre SELECT, elevación
    De SOLO las ciudades
    La elevación de Dónde sectura 500;

   nombre de la elevación
---------------------
 Las Vegas 2174
 Mariposa - 1953
```

Aquí el  `ONLY`palabra clave indica que la consulta debe aplicarse sólo a `cities`, y no ninguna tabla a continuación  `cities`en la jerarquía de herencias. Muchas de las órdenes que ya hemos discutido. `SELECT`,  `UPDATE`y  `DELETE`- apoyo de la  `ONLY`Palabra clave.

También puede escribir el nombre de la tabla con un rastro  `*`especificar explícitamente que se incluyen las tablas descendientes:

```
Nombre SELECT, elevación
    De las ciudades*
    La elevación de Dónde sectura 500;
```

Escrito  `*`no es necesario, ya que este comportamiento es siempre el defecto. Sin  embargo, esta sintaxis sigue siendo compatible para la compatibilidad  con versiones más antiguas donde el default podría ser cambiado.

En algunos casos podría desear saber de qué tabla se originó una fila en particular. Hay una columna del sistema llamada  `tableoid`en cada tabla que pueda indicarle el cuadro de origen:

```
SELECT c.tableoid, c.name, c.elevation
De las ciudades c
DONDE c.elevation no 500;
```

que devuelve:

```
tableoide . . . . . . . .
-----------------------------------------
   139793 . Las Vegas . 2174
   139793 . Mariposa . 1953
   139798 - Madison 845
```

(Si intentas reproducir este ejemplo, probablemente obtendrás diferentes OID numéricos.) Haciendo unirse con  `pg_class`puede ver los nombres de tabla reales:

```
SELECT p.relname, c.name, c.elevation
De las ciudades c, pg.class p
DONDE c.elevation - 500 AND c.tableoid = p.oid;
```

que devuelve:

```
renombre de nombre, elevación de nombre
-----------------------------------------
 ciudades de Las Vegas
 ciudades de Mariposa - 1953
 capitales de Madison 845
```

Otra forma de obtener el mismo efecto es utilizar el  `regclass`tipo alias, que imprimirá la tabla OID simbólicamente:

```
SELECT c.tableoid::regclass, c.name, c.elevation
De las ciudades c
DONDE c.elevation no 500;
```

La herencia no propaga automáticamente los datos de  `INSERT`o o  `COPY`comando a otras tablas en la jerarquía de herencias. En nuestro ejemplo, los siguientes  `INSERT`La declaración fracasará:

```
INSERT INTO ciudades (nombre, población, elevación, estado)
VALUES ('Albany', NULL, NULL, 'NY');
```

Podríamos esperar que los datos de alguna manera se enruten a la  `capitals`mesa, pero esto no sucede:  `INSERT`siempre se inserta exactamente en la tabla especificada. En algunos casos es  posible reorientar la inserción mediante una norma (véase [el capítulo 41](https://www.postgresql.org/docs/current/rules.html)). Sin embargo, eso no ayuda para el caso anterior porque  `cities`mesa no contiene la columna `state`, y por lo tanto el comando será rechazado antes de que la regla pueda ser aplicada.

Todas las restricciones de control y las restricciones no nulos en  una tabla de padres son automáticamente heredadas por sus hijos, a menos que se especifique explícitamente lo contrario con  `NO INHERIT`cláusulas. Otros tipos de limitaciones (restricciones únicas, de clave primaria y de clave externa) no se heredan.

Una tabla puede heredar de más de una tabla de padres, en cuyo caso tiene la unión de las columnas definidas por las tablas matrices. A  estas se añaden las columnas declaradas en la definición de la tabla de  niños. Si el mismo nombre de la columna aparece en varias tablas de  padres, o tanto en una tabla de padres como en la definición del niño,  entonces estas columnas se fusionan para que sólo haya una de esas columnas en la tabla del niño. Para  fusionarse, las columnas deben tener los mismos tipos de datos, de lo  contrario se plantea un error. Las restricciones de control hereditaria y las limitaciones no-nulas se fusionan de una manera similar. Así, por  ejemplo, una columna fusionada no se marcará nill si alguna de las  definiciones de columna de las que procede está marcada no en mosquida.  Las restricciones de cheques se fusionan si tienen el mismo nombre, y la fusión fallará si sus condiciones son diferentes.

La herencia de tabla se establece típicamente cuando se crea la tabla de niños, utilizando la  `INHERITS`cláusula de la  [`CREATE TABLE`](https://www.postgresql.org/docs/current/sql-createtable.html)declaración. Alternativamente, una tabla que ya está definida de una manera  compatible puede tener una nueva relación madre añadiendo, utilizando la  `INHERIT`variante de [`ALTER TABLE`](https://www.postgresql.org/docs/current/sql-altertable.html). Para ello, la nueva tabla de niños ya debe incluir columnas con los  mismos nombres y tipos que las columnas del padre. También debe incluir  restricciones de control con los mismos nombres y establecer expresiones de control que las del padre. Del mismo modo, un vínculo sucesorial se  puede eliminar de un niño utilizando el  `NO INHERIT`variante de `ALTER TABLE`. Añadiendo y eliminando dinámicamente enlaces de herencia como este  puede ser útil cuando la relación de herencia se está utilizando para la partición de la tabla (ver [Sección](https://www.postgresql.org/docs/current/ddl-partitioning.html) 5.11).

Una forma conveniente de crear una tabla compatible que más tarde se hará un nuevo hijo es utilizar el  `LIKE`cláusula en `CREATE TABLE`. Esto crea una nueva tabla con las mismas columnas que la tabla de fuentes. Si hay alguno  `CHECK`las limitaciones definidas en el cuadro de fuentes,  `INCLUDING CONSTRAINTS`opción a  `LIKE`debe especificarse, ya que el nuevo hijo debe tener limitaciones que coinijan al padre para ser considerado compatible.

Una mesa de padres no puede ser deprimida mientras alguno de sus  hijos permanezca. Tampoco se pueden retirar o alterar las limitaciones  de las tablas infantiles si se heredan de las tablas de padres. Si desea quitar una mesa y todos sus descendientes, una manera fácil es dejar la mesa madre con el  `CASCADE`Opción (véase [la sección](https://www.postgresql.org/docs/current/ddl-depend.html) 5.14).

 `ALTER TABLE`propagará cualquier cambio en las definiciones de datos de columnas y comprobará  las restricciones a la jerarquía de herencias. Una vez más, la caída de  columnas de las que dependen de otras tablas sólo es posible cuando se  utiliza el  `CASCADE`opción.  `ALTER TABLE`sigue las mismas reglas para la fusión y rechazo de columnas duplicadas que se aplican durante `CREATE TABLE`.

Las consultas heredan realizan controles de permiso de acceso sólo en la mesa madre. Así, por ejemplo, la concesión  `UPDATE`permiso en el  `cities`tabla implica permiso para actualizar filas en el  `capitals`la mesa, cuando se accede a ella `cities`. Esto preserva la apariencia de que los datos están (también) en la tabla de padres. Pero el  `capitals`La tabla no podía actualizarse directamente sin una subvención adicional.  De manera similar, las políticas de seguridad de la fila de los padres  (véase [la Sección 5.8](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)) se aplican a las filas procedentes de las mesas infantiles durante una  consulta heredada. Las políticas de una tabla de niños, en su caso, se  aplican sólo cuando es la tabla explícitamente nombrada en la consulta; y en ese caso, se ignoran las políticas adjuntas a sus padres.

Las tablas extranjeras (véase [la sección 5.](https://www.postgresql.org/docs/current/ddl-foreign-data.html)12) también pueden ser parte de jerarquías de herencia, ya sea como tablas  de padres o hijos, tal como pueden ser las tablas regulares. Si una mesa extranjera forma parte de una jerarquía de herencias, entonces ninguna  operación que no esté respaldada por la mesa extranjera tampoco se apoya en toda la jerarquía.