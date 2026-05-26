# Tema 1: Introducción a LangChain y Chatbots

En este tema se presentan ejemplos básicos de uso de LangChain para trabajar con modelos de OpenAI. Incluye tres archivos de ejemplo que cubren:

- uso directo de `ChatOpenAI`
- uso de plantillas de prompts con `PromptTemplate`
- creación de una interfaz de chatbot en Streamlit

## Archivos incluidos

### `hello_world.py`
Ejemplo mínimo de una llamada a un modelo con LangChain.

- Importa `ChatOpenAI` de `langchain_openai`
- Crea una instancia de `ChatOpenAI`
- Envía una pregunta simple sobre la llegada del ser humano a la Luna
- Imprime la respuesta del modelo

### `hello_world_avanzado.py`
Ejemplo de uso de `PromptTemplate` para estructurar prompts.

- Importa `ChatOpenAI` y `PromptTemplate`
- Define una plantilla de prompt que solicita saludar al usuario por nombre
- Combina la plantilla con el modelo usando `|`
- Invoca la cadena con un valor para la variable `nombre`
- Imprime el resultado generado

### `streamlit.chatbot.py`
Chatbot básico con interfaz en Streamlit y LangChain.

- Usa `streamlit` para construir la UI
- Permite seleccionar el modelo y la temperatura
- Mantiene el historial de conversación en `st.session_state`
- Define un prompt con contexto de historial
- Muestra respuestas del asistente en tiempo real usando streaming

## Requisitos

Asegúrate de tener:

- `python` instalado
- Paquetes necesarios: `langchain_openai`, `langchain_core`, `streamlit`
- Clave de OpenAI configurada en la variable de entorno `OPENAI_API_KEY`

## Ejecución

1. Ejecutar `hello_world.py`:

```bash
python Tema_1/hello_world.py
```

2. Ejecutar `hello_world_avanzado.py`:

```bash
python Tema_1/hello_world_avanzado.py
```

3. Ejecutar la app de Streamlit:

```bash
streamlit run Tema_1/streamlit.chatbot.py
```

## Objetivo del tema

Aprender los conceptos básicos de LangChain:

- cómo inicializar un modelo con `ChatOpenAI`
- cómo definir y usar plantillas de prompt
- cómo construir una aplicación de chatbot simple con Streamlit

Este tema es una base práctica para avanzar hacia cadenas más complejas, agentes y aplicaciones interactivas con LangChain.
