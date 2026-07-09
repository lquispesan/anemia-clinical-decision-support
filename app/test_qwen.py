from ollama import chat
import time

inicio = time.time()

respuesta = chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "¿Qué es la anemia?"
        }
    ]
)

print(respuesta["message"]["content"])

print(
    "Tiempo:",
    round(time.time() - inicio, 2),
    "segundos"
)