from ollama import chat

from app.rag import RAG
from app.prompts import SYSTEM_PROMPT
import time


class LLM:

    def __init__(self):

        self.rag = RAG()


    def responder(self, pregunta):

        # Medir RAG
        inicio_rag = time.time()
        documentos = self.rag.buscar(
            pregunta,
            cantidad=5
        )
        fin_rag = time.time()
        print(f"Tiempo RAG: {fin_rag - inicio_rag:.2f} segundos")


        contexto = "\n\n".join(
            [
                doc.page_content
                for doc in documentos
            ]
        )
        print("===== DOCUMENTOS RECUPERADOS =====")

        for doc in documentos:
            print("--------------------")
            print(doc.metadata)
            print(doc.page_content[:300])

        print("==============================")


        prompt = SYSTEM_PROMPT.format(
            context=contexto,
            question=pregunta
        )
         # Medir LLM
        inicio_llm = time.time()

        respuesta = chat(
            model="qwen3:4b",
            messages=[
                {
                    "role": "user",
                    "content": "/no_think\n\n" + prompt
                }
            ]
        )
        fin_llm = time.time()
        print(f"Tiempo LLM: {fin_llm - inicio_llm:.2f} segundos")

        return respuesta["message"]["content"]



if __name__ == "__main__":

    asistente = LLM()


    pregunta = (
        "¿Cuál es la importancia de la suplementación de hierro?"
    )


    respuesta = asistente.responder(
        pregunta
    )


    print(respuesta)
