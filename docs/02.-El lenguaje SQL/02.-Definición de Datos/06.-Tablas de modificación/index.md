Cuando creas una tabla y te das cuenta de que cometiste un error, o  los requisitos de la aplicación cambian, puedes dejar la tabla y crearla de nuevo. Pero esta no es una opción conveniente si la tabla ya está  llena de datos, o si la tabla es referenciada por otros objetos de base  de datos (por ejemplo, una restricción de clave extranjera). Por lo  tanto PostgreSQL proporciona una familia de comandos para hacer modificaciones en las  tablas existentes. Tenga en cuenta que esto es conceptualmente distinto  de alterar los datos contenidos en la tabla: aquí estamos interesados en alterar la definición, o estructura, de la tabla.

Puedes:

- Añadir columnas
- Eliminar columnas
- Añádase limitaciones
- Eliminar las restricciones
- Cambiar los valores por defecto
- Cambiar los tipos de datos de la columna
- Renoname de columnas
- Tablas de nombres

Todas estas acciones se realizan utilizando el comando [ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html), cuya página de referencia contiene detalles más allá de los que se dan aquí.