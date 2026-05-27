from langchain_core.prompts import PromptTemplate

template="""Eres un experto en marketin digital. 
    Sugiere un logotipo creativo para un producto {producto}.
    El logotipo debe ser simple, memorable y reflejar la esencia del producto."""

prompt = PromptTemplate(template=template,
                        input_variables=["producto"])

prompt_completo = prompt.format(producto="Mouse Gaming de ultima generación")
print(prompt_completo)