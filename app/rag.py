from pathlib import Path

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_DIR = BASE_DIR / "data" / "chroma"


class RAG:

    def __init__(self):

        embeddings = OllamaEmbeddings(
            model="nomic-embed-text"
        )


        self.db = Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=embeddings
        )


    def buscar(self, pregunta, cantidad=5):

        resultados = self.db.similarity_search(
            pregunta,
            k=cantidad
        )


        return resultados



if __name__ == "__main__":

    rag = RAG()

    pregunta = "¿Qué es la anemia ferropénica?"

    documentos = rag.buscar(pregunta)


    for i, doc in enumerate(documentos):

        print("\n----------------")
        print(f"Resultado {i+1}")
        print("----------------")

        print(doc.page_content[:500])

        print(
            "Fuente:",
            doc.metadata
        )