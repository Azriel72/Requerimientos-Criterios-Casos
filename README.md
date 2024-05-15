# Requerimientos-Criterios-Casos
Esta es la asignación colocada en el campus virtual por el docente LORENZO SOLANO MARTINEZ

¿Qué es un Coding Dojo? referencia https://lorenzosolano.com/what-is-coding-dojo/

    Un "Codigo Dojo" es un espacio donde los desarrolladores se reunen para trabajar en un mismo problema desafiante. El desafío puede ser un problema algorítmico a resolver o una necesidad de implementar. Cada dojo de codificación se centra en un tema en particular y representa el objetivo de la sesión.

Diferencia entre Requerimientos, Criterios de Aceptación y Escenarios de Prueba. Dar ejemplos a partir de un problema distinto a la referencia. Referencia https://lorenzosolano.com/requirements-acceptance-criteria-and/

    Para empezar, un requerimiento es cualquier cosa que proponga una restricción o necesidad del software a desarrollar para dar así una solución al problema general. Por otro lado, los criterios de aceptación son enunciados que, en general, dictan si una determinada parte del software cumple o no con el requerimiento establecido. Finalmente, los escenarios de prueba son aquellos los cuales permiten ejemplificar el comportamiento esperado del software el cual si cumple con los requerimientos establecidos. 
   
    Un ejemplo que ilustra el comportamiento de estos tres conceptoss es el siguiente. Suponga que se desea crear un programa para gestionar las tareas y procesos de un entorno educativo. Un requerimiento del sistem es que debe ser capaz de analizar el progreso y las preferencias de aprendizaje de cada estudiante. Además, como criterio de aceptación, debe ser capaz de recomendar ecursos educativos relevantes para cada estudiante. Como escenario de prueba, si un estudiante utiliza por primera vez el sistema y accede a la función de asistente de estudio se espera que el sistema le recomiende recursos educativos relevantes para su perfil.
    
De dos ejemplos de requerimientos no-funcionales, y especifique cual es su categoría (seguridad, performance, portabilidad, etc.)

      Sabiendo que los requerimientos no funcionales son aquellos que restringen el software, dado el ejemplo anterior, tenemos: El sistema debe utilizar cifrado de extremo a extremo para proteger la confidencialidad de los datos del estudiante durante la transmisión y el almacenamiento (esto es un requetimiento de seguridad). Además, La interfaz de usuario del sistema debe ser accesible para usuarios con discapacidades visuales, cumpliendo con las pautas de accesibilidad web internacionales (esto es un requerimiento de usabilidad/accesibilidad).
¿Qué es TDD?

      TDD (Test Driven Development) es una metodología de desarrollo de software que se basa en escribir pruebas automatizadas antes de escribir el código como tal. Primero se escribe cuales serán los escenarios de prueba, luego se realiza el código y finaliza con la prueba de los escenarios de prueba previamente establecidos.
¿Que son pruebas unitarias automatizadas?

     Las pruebas automatizadas son un tipo de prueba en el desarrollo de software que se enfoca en verificar el comportamiento y la funcionalidad de unidades individuales de código, generalmente funciones, métodos o clases, de manera automatizada.
¿Cual fue el 1er framework de pruebas unitarias y para cual lenguaje fue creado?

     EL primer framework de pruebas unitarias fue el llamado SUnit lanzado en 1987  por Kent Beck y otros desarrolladores. El lenguaje para cual se creó este framework fue Smalltalk code.
Describa los componentes de la arquitectura xUnit

     La arquitectura xUnit consta de varios componentes clave que trabajan juntos para facilitar el proceso de escritura, ejecución y reporte de pruebas unitarias en un framework de pruebas. Estos componentes incluyen el Fixture, que establece las condiciones iniciales para las pruebas; el Test Case, que contiene una o más pruebas unitarias; el Test Suite, que agrupa test cases relacionados para ejecutarlos juntos; el Test Runner, que ejecuta las pruebas y reporta los resultados; las Assertions, que verifican condiciones durante la ejecución de una prueba; y los Reporters, que generan informes detallados sobre los resultados de las pruebas.
Indique al menos tres desventajas de las pruebas unitarias automatizadas

     Costo inicial y mantenimiento, cobertura limitada y falsos positivos y negativos.
Indique al menos tres ventajas de las pruebas unitarias automatizadas

     Detección temprana de errores, retroalimentación rápida y refactorización segura.

1. Requerimientos:

R1: Conversión Decimal a Romano

    El sistema debe convertir números decimales en su equivalente numeral romano.

R2: Rango de Entrada Válida

    El sistema debe aceptar números enteros en el rango de 1 a 3999 para la conversión.

R3: Validación de Entrada

    El sistema debe validar que la entrada sea un número entero dentro del rango válido.

R4: Salida del Resultado

    El sistema debe mostrar el número romano equivalente como resultado de la conversión.

2. Criterios de Aceptación:

C1: Conversión Correcta

    El sistema debe convertir correctamente números decimales en su equivalente numeral romano, siguiendo las reglas establecidas.

C2: Validación de Entrada

    El sistema debe mostrar un mensaje de error si la entrada no es un número entero válido o está fuera del rango aceptado.

C3: Rango de Entrada

    El sistema debe aceptar números decimales en el rango válido (1 a 3999) y rechazar cualquier entrada fuera de este rango.

3. Casos de Prueba:

Casos de Prueba Unitarios (Caja Blanca - Código):

    Prueba de Conversión Correcta
        Entrada: 10
        Salida Esperada: X

    Prueba de Límites Inferiores
        Entrada: 1
        Salida Esperada: I

    Prueba de Límites Superiores
        Entrada: 3999
        Salida Esperada: MMMCMXCIX

    Prueba de Validación de Entrada Incorrecta
        Entrada: ABC
        Salida Esperada: Mensaje de error: "Entrada no válida. Por favor, ingrese un número entero."

    Prueba de Rango de Entrada Inválido
        Entrada: 4000
        Salida Esperada: Mensaje de error: "Número fuera de rango. Por favor, ingrese un número entre 1 y 3999."

Casos de Prueba End-To-End (Desde el UI):

    Prueba de Conversión Correcta
        Entrada: 50
        Salida Esperada: L

    Prueba de Entrada Inválida
        Entrada: -5
        Salida Esperada: Mensaje de error en la interfaz: "Entrada no válida. Por favor, ingrese un número entero positivo."
