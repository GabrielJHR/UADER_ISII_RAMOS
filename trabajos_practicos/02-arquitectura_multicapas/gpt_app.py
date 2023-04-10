#!/usr/bin/python
import openai
import pyreadline3

# Se configura el objeto readline para obtener el historial
readline = pyreadline3.Readline()
readline.set_history_length(1000)

# Configura la tecla de navegación de historial
readline.parse_and_bind("up: history-search-backward")

#……. [ mas Código de inicialización aqui ] …………
# Se ha puesto la api key generada por open ia en un archivo externo llamado 'apy_key'
# con el objetivo de que no filtrar la api key en el repositorio publico de Github
# al hacer un git add se va a ignorar el archivo.
with open("api_key", "r") as file:
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

try:
    while(True):
        #.....[otra lógica necesaria – el texto del prompt debe colocarse en userText]…..
        # Set up the model and prompt
        userText = input("You: ")

        if(userText):
            try:
                try:
                    completion = openai.Completion.create(
                        engine=MODEL_ENGINE,
                        prompt=userText,
                        max_tokens=MAX_TOKENS,
                        n=NMAX,
                        top_p=TOP_P,
                        frequency_penalty=FREQ_PENALTY,
                        presence_penalty=PRES_PENALTY,
                        temperature=TEMPERATURE,
                        stop=STOP
                    )

                    response = completion.choices[0].text
                    print('ChatGPT: ', response)

                    # Se agrega la pregunta anterior al historial
                    readline.add_history(userText)
                except openai.error.AuthenticationError:
                    print("Error de autenticación: verifique su clave de API de OpenAI.")
                except openai.error.APIConnectionError:
                    print("Error de conexión: no se pudo conectar a la API de OpenAI.")
                except openai.error.APIError:
                    print("Error de API: se produjo un error al procesar la solicitud.")
                except openai.error.RateLimitError:
                    print("Error de límite de tasa: se alcanzó el límite de solicitudes a la API de OpenAI.")
                except Exception as e:
                    print("Error: ", e)

            except Exception as e:
                print("Error al procesar la entrada del usuario: ", e)
        else:
            print("La entrada esta vacia")
except KeyboardInterrupt:
    print("\nInterrupción de teclado detectada. Saliendo del programa...")