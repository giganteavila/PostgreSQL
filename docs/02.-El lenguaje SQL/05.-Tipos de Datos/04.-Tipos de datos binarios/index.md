El  `bytea`tipo de datos permite el almacenamiento de cadenas binarias; véase [Tabla 8](https://www.postgresql.org/docs/current/datatype-binary.html#DATATYPE-BINARY-TABLE).6.

**Cuadro 8.6. Tipos de datos binarios**

| Nombre  | Tamaño de almacenamiento               | Descripción                         |
| ------- | -------------------------------------- | ----------------------------------- |
| `bytea` | 1 o 4 bytes más la cadena binaria real | cuerda binaria de longitud variable |

Una cuerda binaria es una secuencia de octets (o bytes). Las  cuerdas binarias se distinguen de las cuerdas de carácter de dos  maneras. En primer lugar, las cadenas binarias permiten específicamente  almacenar octets de valor cero y otros non-printableoctets no imprimibles (generalmente, octets fuera del rango decimal 32 a 126). Las cadenas de caracteres desautoran los octets cero, y también desautoran cualquier  otro octeto y secuencias de valores octetos que no sean válidos de  acuerdo con la codificación de conjunto de caracteres seleccionada de la base de datos. En segundo lugar, las operaciones en las cadenas  binarias procesan los bytes reales, mientras que el procesamiento de  cadenas de caracteres depende de la configuración local. En resumen, las cadenas binarias son apropiadas para almacenar los datos que el  programador considera como "bytes brutos", mientras que las cadenas de caracteres son apropiadas para almacenar texto.

El  `bytea`type soporta dos formatos para la entrada y salida: hexformato hex y formato PostgreSQL 's histórico- escape. Ambos son siempre aceptados en las aportaciones. El formato de salida depende del parámetro de configuración [bytea-output ](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-BYTEA-OUTPUT); el valor predeterminado es hex. (Ten en cuenta que el formato hex se introdujo en PostgreSQL 9.0; versiones anteriores y algunas herramientas no lo entienden.)

El  SQLestándar define un tipo de cadena binario diferente, llamado  `BLOB`o o `BINARY LARGE OBJECT`. El formato de entrada es diferente de `bytea`, pero las funciones y los operadores proporcionados son en su mayoría los mismos.