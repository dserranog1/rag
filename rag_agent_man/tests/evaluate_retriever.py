from deepeval import evaluate
from deepeval.metrics import (
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    ContextualRelevancyMetric,
)

from rag_agent_man.rag import RAG
from rag_agent_man.tests.utils import create_deep_eval_test_cases, parse_test_data


def main():
    rag = RAG()
    questions, ground_truth_answers = parse_test_data()
    retrieved_documents = []
    generated_answers = []

    for question in questions:
        context = rag.retrieve(query=question, as_list=True)
        retrieved_documents.append(context)
        context_string = " ".join(context)
        result = rag.generate(question, context_string)
        generated_answers.append(result.content)

    test_cases = create_deep_eval_test_cases(
        questions, ground_truth_answers, generated_answers, retrieved_documents
    )

    contextual_precision_metric = ContextualPrecisionMetric(
        threshold=0.7,
        include_reason=True,
    )
    contextual_recall_metric = ContextualRecallMetric(
        threshold=0.7, include_reason=True
    )
    contextual_relevancy_metric = ContextualRelevancyMetric(
        threshold=0.7, include_reason=True
    )

    evaluate(
        test_cases=test_cases,
        metrics=[
            contextual_precision_metric,
            contextual_recall_metric,
            contextual_relevancy_metric,
        ],
    )

if __name__ == "__main__":
    main()