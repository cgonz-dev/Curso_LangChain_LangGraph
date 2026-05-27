from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate


# Configuración de la página de la app
st.set_page_config(page_title="Chatbot Basico", page_icon="🤖")
if st.button("🗑️ Nueva conversación"):
    st.session_state.messages = []
    st.rerun()
st.title("🤖 Chatbot Basico con Langchain y Streamlit")

st.markdown(
    "Este es un ejemplo de un chatbot básico utilizando Langchain y Streamlit. "
    "Escribe tu mensaje y el chatbot responderá utilizando un modelo de lenguaje de OpenAI."
)

with st.sidebar:
    st.header("Configuración")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
    model_name = st.selectbox("Modelo", ["gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"])

    personalidad = st.selectbox(
        "Personalidad del Asistente",
        [
            "Útil y amigable",
            "Profesional y formal", 
            "Casual y relajado",
            "Experto técnico",
            "Creativo y divertido"
        ]
    )


# Inicializar el modelo de lenguaje
chat_model = ChatOpenAI(
    model=model_name,
    temperature=temperature
)

system_messages = {
        "Útil y amigable": "Eres un asistente útil y amigable llamado ChatBot Pro. Responde de manera clara y concisa.",
        "Profesional y formal": "Eres un asistente profesional y formal. Proporciona respuestas precisas y bien estructuradas.",
        "Casual y relajado": "Eres un asistente casual y relajado. Habla de forma natural y amigable, como un buen amigo.",
        "Experto técnico": "Eres un asistente experto técnico. Proporciona respuestas detalladas con precisión técnica.",
        "Creativo y divertido": "Eres un asistente creativo y divertido. Usa analogías, ejemplos creativos y mantén un tono alegre."
    }

# Inicializar el historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []


chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_messages[personalidad]),
    ("human", "Historial de conversación:\n{historial}\n\nPregunta actual: {mensaje}")
])

# Crear cadena usando LCEL
cadena = chat_prompt_template | chat_model

# Mostrar el historial de mensajes en la interfaz
for msg in st.session_state.messages:
    if isinstance(msg, SystemMessage):
        continue

    role = "assistant" if isinstance(msg, AIMessage) else "user"

    with st.chat_message(role):
        st.markdown(msg.content)

# Entrada del usuario
pregunta = st.chat_input("Escribe tu mensaje")

if pregunta:
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(pregunta)

    try:
        # Convertir historial a texto
        historial_texto = "\n".join([
            f"Usuario: {msg.content}" if isinstance(msg, HumanMessage)
            else f"Asistente: {msg.content}"
            for msg in st.session_state.messages
        ])

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            # Streaming de la respuesta
            for chunk in cadena.stream({
                "mensaje": pregunta,
                "historial": historial_texto
            }):
                full_response += chunk.content
                response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(full_response)

        # Guardar mensajes en historial
        st.session_state.messages.append(HumanMessage(content=pregunta))
        st.session_state.messages.append(AIMessage(content=full_response))

    except Exception as e:
        st.error(f"Error al generar respuesta: {str(e)}")
        st.info("Verifica que tu API Key de OpenAI esté configurada correctamente.")