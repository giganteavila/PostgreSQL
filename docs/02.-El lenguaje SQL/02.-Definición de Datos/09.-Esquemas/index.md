Un grupo de bases de datos PostgreSQL contiene una o más bases de datos nombradas. Los roles y algunos otros  tipos de objetos se comparten en todo el clúster. Una conexión cliente  al servidor sólo puede acceder a los datos en una sola base de datos, la especificada en la solicitud de conexión.

### Nota

Los usuarios de un grupo no tienen necesariamente el privilegio  de acceder a cada base de datos del grupo. Compartir nombres de roles  significa que no puede haber diferentes roles nombrados, digamos,  `joe`en dos bases de datos en el mismo clúster; pero el sistema se puede configurar para permitir  `joe`acceso a sólo algunas de las bases de datos.

Una base de datos contiene una o más *esquemas* llamados, que a su vez contienen tablas. Los esquemas también contienen otros tipos de objetos mencionados, incluyendo tipos de datos,  funciones y operadores. El mismo objeto se puede utilizar en diferentes  esquemas sin conflicto; por ejemplo, ambos  `schema1`y  `myschema`puede contener tablas nombradas `mytable`. A diferencia de las bases de datos, las esquemas no se separan  rígidamente: un usuario puede acceder a objetos en cualquiera de los  esquemas de la base de datos a la que están conectados, si tienen  privilegios para hacerlo.

Hay varias razones por las que uno podría querer usar esquemas:

- Permitir que muchos usuarios usen una base de datos sin interferir entre sí.
- Organizar objetos de base de datos en grupos lógicos para hacerlos más manejables.
- Las aplicaciones de terceros se pueden poner en esquemas separados para que no colisionen con los nombres de otros objetos.

Los esquemas son análogos a los directorios a nivel del sistema operativo, excepto que los esquemas no pueden ser anidados.