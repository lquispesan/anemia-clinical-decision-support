from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma

from langchain_ollama import OllamaEmbeddings


BASE_DIR = Path(__file__).resolve().parent.parent

DOCS_DIR = BASE_DIR / "docs"

CHROMA_DIR = BASE_DIR / "data" / "chroma"


def cargar_documentos():

    documentos = []

    for archivo in DOCS_DIR.rglob("*"):

        if archivo.suffix.lower() == ".pdf":

            loader = PyPDFLoader(
                str(archivo)
            )

            docs = loader.load()


        elif archivo.suffix.lower() == ".md":

            loader = TextLoader(
                str(archivo),
                encoding="utf-8"
            )

            docs = loader.load()


        else:
            continue


        # Agregar metadata automática

        for doc in docs:

            doc.metadata["categoria"] = archivo.parent.name

            doc.metadata["archivo"] = archivo.name


        documentos.extend(docs)


    return documentos



def crear_base_vectorial():

    print("Cargando documentos...")

    documentos = cargar_documentos()


    print(
        f"Documentos encontrados: {len(documentos)}"
    )


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )


    chunks = splitter.split_documents(
        documentos
    )


    print(
        f"Chunks creados: {len(chunks)}"
    )


    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )


#    Chroma.from_documents(
#        documents=chunks,
#        embedding=embeddings,
#        persist_directory=str(CHROMA_DIR)
#    )

    db = Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=embeddings
    )


    batch_size = 10

    for i in range(0, len(chunks), batch_size):

        batch = chunks[i:i + batch_size]

        print(
          f"Procesando chunks {i+1}-{i+len(batch)} de {len(chunks)}"
        )

    db.add_documents(batch)


    print("Base vectorial creada correctamente")

    print(
        "Base vectorial creada correctamente"
    )



if __name__ == "__main__":

    crear_base_vectorial()