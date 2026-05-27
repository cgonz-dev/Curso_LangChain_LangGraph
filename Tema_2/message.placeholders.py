from langchain.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    ("system",("Eres un asistente util que mantiene el contexto de la conversación y responde a las preguntas del usuario de manera clara y concisa.")),
    MessagesPlaceholder(variable_name="historial"),
    ("human",("Usuario: {pregunta_actual}"))
])

historial_de_conversacion = [
    HumanMessage(content="Usuario: Hola, ¿Cómo estás?"),
    AIMessage(content=" IA: ¡Hola! Estoy bien, gracias por preguntar. ¿En qué puedo ayudarte hoy?"),
    HumanMessage(content="Usuario: ¿Cuál es la capital de Francia?"),
    AIMessage(content=" IA: La capital de Francia es París.")
    ]

mensajes = chat_prompt.format_messages(
    historial = historial_de_conversacion,
    pregunta_actual = "¿Puedes decirme algo interesante sobre los esports?"
)

for m in mensajes:
    print(f"{m.content}")