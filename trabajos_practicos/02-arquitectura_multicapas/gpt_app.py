"""
Este modulo hace llamadas a la api de ChatGPT
"""
import openai
import pyreadline3
import sys

# Se configura el objeto readline para obtener el historial
readline = pyreadline3.Readline()
readline.set_history_length(1000)

# Configura la tecla de navegación de historial
readline.parse_and_bind("up: history-search-backward")

# ……. [ mas Código de inicialización aqui ] …………
# Se ha puesto la api key generada por open ia en un archivo externo llamado 'apy_key'
# con el objetivo de que no filtrar la api key en el repositorio publico de Github
# al hacer un git add se va a ignorar el archivo.
with open("api_key", "r", encoding='utf-8') as file:
    openai.api_key = file.readline()

TOP_P = 1
FREQ_PENALTY = 0
PRES_PENALTY = 0
STOP = None
MAX_TOKENS = 1024
TEMPERATURE = 0.75
NMAX = 1
MODEL_ENGINE = "text-davinci-003"

# Se define el buffer para almacenar tanto las preguntas como las respuestas
# dadas por ChatGPT
buffer = ""

if len(sys.argv) > 1:
    ARGUMENTO = sys.argv[1]
else:
    ARGUMENTO = ""

try:
    while True:
        # .....[otra lógica necesaria – el texto del prompt debe colocarse en userText]…..
        # Set up the model and prompt
        # Se obtiene la entrada del usuario y se asigna a la variable userText
        userText = input("You: ")

        # Si la entrada del usuario no está vacía, se procesa.
        if userText:
            try:
                # Se verifica si el usuario o ChatGPT ha indicado que la conversación está en curso
                if "--convers" in ARGUMENTO:
                    # Si se indica que la conversación está en curso, se agrega la entrada del
                    # usuario al buffer y se muestra la respuesta de ChatGPT
                    buffer += userText
                else:
                    # Si no se indica que la conversación está en curso, se sobrescribe el contenido
                    # del buffer con la entrada del usuario actual
                    buffer = userText

                # Se envía una solicitud a OpenAI para obtener la respuesta del modelo.
                # Se utiliza la API Key que se encuentra en el archivo "api_key"
                completion = openai.Completion.create(
                    engine=MODEL_ENGINE,
                    prompt=buffer,
                    max_tokens=MAX_TOKENS,
                    n=NMAX,
                    top_p=TOP_P,
                    frequency_penalty=FREQ_PENALTY,
                    presence_penalty=PRES_PENALTY,
                    temperature=TEMPERATURE,
                    stop=["You:", "chatGPT:"]
                )

                # Se obtiene la respuesta del modelo y se almacena en la variable "response"
                response = completion.choices[0].text

                # Se muestra la respuesta del modelo en la consola
                print(f"chatGPT: {response}\n\n")

                # Se agrega la respuesta del modelo al buffer
                buffer += response

                # Se agrega la pregunta anterior del usuario al historial de readline
                readline.add_history(userText)

            # Se manejan posibles errores que pueden ocurrir al interactuar con la API de OpenAI
            except openai.error.AuthenticationError:
                print("Error de autenticación: verifique su clave de API de OpenAI.")
            except openai.error.APIConnectionError:
                print("Error de conexión: no se pudo conectar a la API de OpenAI.")
            except openai.error.APIError:
                print("Error de API: se produjo un error al procesar la solicitud.")
            except openai.error.RateLimitError:
                print(
                    "Error de límite de tasa: se alcanzó el límite de solicitudes a la API de OpenAI.")
            except Exception as e:
                print("Error: ", e)

        else:
            # Si la entrada del usuario está vacía, se muestra un mensaje en la consola.
            print("La entrada esta vacia")
except KeyboardInterrupt:
    print("\nInterrupción de teclado detectada. Saliendo del programa...")
