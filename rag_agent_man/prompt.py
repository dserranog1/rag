from langchain_core.prompts import PromptTemplate

template = """Responde a la pregunta de manera precisa y utilizando únicamente la información que se encuentra en el contexto. 
Si la información no está disponible, simplemente responde "Lo siento, no lo sé".
No hagas suposiciones ni inventes respuestas. Mantén tus respuestas concisas.

Contexto: {context}

Pregunta: {question}

Respuesta:"""


def get_promt():
    return PromptTemplate.from_template(template)
