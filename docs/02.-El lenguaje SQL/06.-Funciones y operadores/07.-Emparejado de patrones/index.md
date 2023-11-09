Hay tres enfoques separados para la coincidencia de patrones proporcionado por PostgreSQL: el tradicional   SQL`LIKE`operador, el más reciente  `SIMILAR TO`operador (añadido en SQL:1999), y POSIX- expresiones regulares. Aparte de lo básico, esta cadena coincide con este patrón? - los operadores, las funciones están disponibles para extraer o  reemplazar subcadeaciones coincidentes y para dividir una cadena en  lugares que coincían.

### Tip

Si tiene necesidades de emparesiones que van más allá de esto,  considere escribir una función definida por el usuario en Perl o Tcl.

### Precaución

Si bien la mayoría de las búsquedas de expresión regulares se  pueden ejecutar muy rápidamente, se pueden inventar expresiones  regulares que toman cantidades arbitrarias de tiempo y memoria para  procesar. Tenga cuidado de aceptar patrones de búsqueda de expresión  regular de fuentes hostiles. Si usted debe hacerlo, es recomendable  imponer una declaración de tiempo de tiempo.

Búsquedas usando  `SIMILAR TO`los patrones tienen los mismos riesgos para la seguridad, desde  `SIMILAR TO`proporciona muchas de las mismas capacidades que POSIX- expresiones regulares.

 `LIKE`Las búsquedas, siendo mucho más simples que las otras dos opciones, son más seguras de usar con fuentes de patrones posiblemente hostiles.

Los operadores de los tres tipos que coinciden con el patrón no  soportan las recopilaciones no deterministas. Si es necesario, aplique  una recopilación diferente a la expresión para trabajar en torno a esta  limitación.