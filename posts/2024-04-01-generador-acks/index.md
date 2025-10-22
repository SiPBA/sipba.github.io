---
title: "Generador de ACKs para proyectos de la Agencia Estatal de Investigación"
date: "2024-04-01"
categories: 
  - "ciencia"
  - "tecnologia"
tags: 
  - "acks"
  - "burocracia"
---

# El marco normativo

**Burocracia**.

Ese mal al que nos enfrentamos el personal investigador desde tiempos inmemoriales. Uno de los últimos trends en este aspecto es una estructura rígida para la justificación de las diferentes fuentes de financiación, especialmente desde entidades públicas. Cada convocatoria puede tener sus propias normativas, formatos y criterios de evaluación, lo que exige una atención minuciosa y un entendimiento detallado de cada conjunto de reglas aplicables.

A veces, navegar en este proceloso mar, hace que dediquemos bastante tiempo a intentar adaptarnos a los [requisitos de publicidad de ayudas](https://www.aei.gob.es/sites/default/files/inline-files/20240301_Instrucciones-comunicacion-publicidad-ayudas%20OK.pdf) en documentos con decenas de páginas, en los que el tipo de estructura varía según el año de convocatoria de la misma ayuda, y, por supuesto, con traducciones manifiestamente mejorables.

# La solución

Aún así, se trata de una serie de casos debidamente definidos en el pdf, por lo que crear una interfaz básica en HTML (con simpleCSS.org para el estilo) y que modificara el output en javascript era sencillo. ¿El resultado? [AQUÍ](https://pakitochus.github.io/generador_ayudas_aei/) ,

![Interfaz (con modo oscuro). ](images/paste-1.png)

Por cierto, también genera el enlace a la etiqueta. En futuras versiones tengo ya dos cosas pendientes: la ampliación para justificar diversas ayudas en un mismo texto, y generar una etiqueta con el nombre de proyecto (supongo que usar HTML canvas para eso puede ser buena idea).

Mientras, me sirve para verificar que, al menos en mi caso, los ACKS están bien puestos. Espero que os sirva a los demás también.