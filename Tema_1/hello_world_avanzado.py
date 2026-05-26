from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

chat = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

plantilla = PromptTemplate.from_template(
    "Saluda al usuario con su nombre.\nNombre del Usuario: {nombre}\nAsistente:"
)

chain = plantilla | chat

resultado = chain.invoke({"nombre": "Cristopher"})

print(resultado.content)