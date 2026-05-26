from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_openai import ChatOpenAI
import json

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def preprocess_text(text):
    """Limpia el texto eliminando espacios extras y limitando longitud"""
    text = text.strip()
    return text[:500] # Limita a 500 caracteres

preprocessor = RunnableLambda(preprocess_text) # Paso 1: Preprocesar el texto

def generate_summary(text):
    """Genera un resumen conciso del texto"""
    prompt = f"Analiza el sentimiento del siguiente texto. Identifica si el tono general es positivo, negativo o neutral, y resume tu conclusión en una sola oración: {text}"
    response = llm.invoke(prompt)
    return response.content

summary_branch = RunnableLambda(generate_summary)

def analyze_sentiment(text):
    """Analiza el sentimiento y devuelve resultado estructurado""" 
    prompt = f"""Analiza el sentimiento del siguiente texto.
    Responde ÚNICAMENTE en formato JSON válido:
    {{"sentimiento": "positivo|negativo|neutro", "razon": "justificación breve"}}
    
    Texto: {text}"""
    
    response = llm.invoke(prompt)
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {"sentimiento": "neutro", "razon": "Error en análisis"}

sentiment_branch = RunnableLambda(analyze_sentiment)

def merge_results(data):
    """Combina los resultados de ambas ramas en un formato unificado"""
    return {
        "resumen": data["resumen"],
        "sentimiento": data["sentimiento_data"]["sentimiento"],
        "razon": data["sentimiento_data"]["razon"]
    }

merger = RunnableLambda(merge_results)



parallel_analysis = RunnableParallel({
    "resumen": summary_branch,
    "sentimiento_data": sentiment_branch
})

#Cadena completa
chain = preprocessor | parallel_analysis | merger

review_batch = [
    "Me encantó el producto, superó mis expectativas y el servicio fue excelente.",
    "El producto llegó tarde y estaba dañado, muy decepcionado con la compra.",
    "El producto es aceptable, cumple su función pero no destaca en nada."
]
result_batch = chain.batch(review_batch)
print(result_batch)