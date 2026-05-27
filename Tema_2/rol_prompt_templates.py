from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

plantilla_sistema = SystemMessagePromptTemplate.from_template( "" \
    "Eres un rol {rol} Especializado en {especialidad}. Responde de manera {tono}" \
)

plantilla_humano = HumanMessagePromptTemplate.from_template("Mi pregunta sobre {tema} es: {pregunta}")

chat_prompt = ChatPromptTemplate.from_messages([
    plantilla_sistema,
    plantilla_humano
])

mensajes = chat_prompt.format_messages(
    rol = "Coach de Valorant",
    especialidad = "Estrategia de juego y análisis de partidas",
    tono = "clara, concisa y profesional",
    tema = "Ataque en Haven side A",
    pregunta = "¿Cuales son las mejores tácticas para atacar en Haven side A?")
for m in mensajes:
    print(f"{m.content}")