from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

from rag_agent_man.rag import RAG

test_data = [
    {
        "question": "Que perfil debería tener un aspirante a la carrera de administración de sistema informáticos?",
        "expected_answer": "Las tecnologías informáticas y su continua actualización. "
        "Desarrollar habilidades para generar y plantear alternativas de acción y toma de decisiones. "
        "Desplegar habilidades que permitan establecer buenas relaciones interpersonales y comunicación efectiva con su entorno. "
        "Buscar la excelencia y calidad en su formación para ser un profesional que contribuya al desarrollo de las organizaciones modernas. "
        "Habilidades para establecer adecuadas relaciones interpersonales. "
        "Aptitudes para comunicarse efectivamente con los demás, en forma oral y escrita. "
        "Interés por la continua actualización, interpretación y evolución del saber profesional. "
        "Alto sentido de responsabilidad y sensibilidad social.",
    },
    {
        "question": "Que perfil debería tener un aspirante a la carrera de matemáticas?",
        "expected_answer": "Aptitudes de tipo analítico y de cálculo matemático. "
        "Interés científico. "
        "Inclinación preferencial por el manejo de las matemáticas y de la física. "
        "Aptitudes para enfrentar problemas desde diferentes puntos de vista. "
        "Interés permanente en actualización. ",
    },
    {
        "question": "Que perfil debería tener un aspirante a la carrera de administración de empresas?",
        "expected_answer": "Interés en desarrollar habilidades de liderazgo. "
        "Espíritu Emprendedor. "
        "Actitud crítica y analítica. "
        "Motivación hacia el trabajo interdisciplinar. "
        "Orientación hacia la solución de problemas. "
        "Disposición hacia las relaciones interpersonales y comunicativas. ",
    },
    {
        "question": "Que perfil debería tener un aspirante a la carrera de administración de matemáticas?",
        "expected_answer": "Lo siento, no lo sé.",
    },
]




def test_answer_relevancy():
    rag = RAG()
    test_item = test_data[0]
    relevant_docs = rag.retrieve(test_item["question"], as_list=True)
    response = rag.generate(test_item["question"], relevant_docs)
    answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5)
    test_case = LLMTestCase(
        input=test_item["question"],
        actual_output=response.content,
        retrieval_context=relevant_docs
    )
    assert_test(test_case, [answer_relevancy_metric])