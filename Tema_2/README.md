# Tema 2: Análisis de Sentimientos con LangChain

Este tema muestra cómo usar LangChain para analizar el sentimiento de textos y estructurar resultados usando `RunnableLambda` y `RunnableParallel`.

## Archivos incluidos

### `analisis_de_sentimientos.py`
Ejemplo principal que realiza un flujo de análisis de sentimiento.

- Preprocesa texto con una función simple que elimina espacios adicionales y limita la longitud.
- Genera un resumen conciso del sentimiento usando un prompt hacia `ChatOpenAI`.
- Realiza un segundo análisis que devuelve un JSON estructurado con el sentimiento (`positivo`, `negativo` o `neutro`) y una razón breve.
- Ejecuta ambas ramas en paralelo usando `RunnableParallel`.
- Combina los resultados en un único objeto con `resumen`, `sentimiento` y `razon`.
- Ejecuta un lote de ejemplo con tres reseñas distintas.

### `ejemplo_runnables.py`
Ejemplo sencillo de cómo encadenar `RunnableLambda`.

- Define un primer paso que formatea un número.
- Define un segundo paso que duplica el texto resultante.
- Combina ambos pasos en una cadena y la invoca con un valor de prueba.

## Conceptos aprendidos

- Uso de `ChatOpenAI` para invocar prompts con LangChain.
- Creación de funciones reutilizables con `RunnableLambda`.
- Ejecución de múltiples tareas en paralelo con `RunnableParallel`.
- Manejo básico de respuesta JSON y errores de parseo.
- Cómo unir resultados de varias ramas en un solo flujo.

## Requisitos

Asegúrate de tener:

- `python` instalado
- Paquetes necesarios: `langchain_openai`, `langchain_core`
- Clave de OpenAI configurada en la variable de entorno `OPENAI_API_KEY`

## Ejecución

1. Ejecutar el análisis de sentimientos:

```bash
python Tema_2/analisis_de_sentimientos.py
```

2. Ejecutar el ejemplo de runnables:

```bash
python Tema_2/ejemplo_runnables.py
```

## Objetivo del tema

Entender cómo construir flujos de procesamiento de texto con LangChain, combinar resultados de análisis de sentimiento y trabajar con pipelines paralelos para obtener resultados más rápidos y estructurados.
