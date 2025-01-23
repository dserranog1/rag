TEMPLATE = """Responde a la pregunta de manera precisa y utilizando únicamente la información que se encuentra en el contexto. 
Si la información no está disponible, responde: "Lo siento, no lo sé", sin agregar nada.
No hagas suposiciones ni inventes respuestas. Mantén tus respuestas concisas, simples, y no agregues nada que no se encuentre en el contexto.
De ser posible, utiliza la información del contexto textualmente.

***Contexto***: {context}

***Pregunta***: {question}

Respuesta:"""
