#!/usr/bin/env python
import sys
import warnings

from chat.crew import PDFCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Executa a crew responsável por criar PDFs.
    """
    inputs = {
        "title": "Relatório de Teste",
        "text": "Este é um relatório gerado para testar a ferramenta de criação de PDFs.",
        "image_path": "inputs/imagem_teste.png",  # Certifique-se de ter a imagem nesse caminho
        "output_path": "inputs/output.pdf"  # Caminho onde o PDF gerado será salvo
    }
    PDFCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Chat().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Chat().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Chat().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
