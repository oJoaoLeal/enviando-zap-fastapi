from fastapi import FastAPI
import pywhatkit as wa

app = FastAPI()


@app.get("/zap")
def sendwhatmsg_instantly(numero: str, msg: str, temp_espera: int = 15, fecha_janela: bool = False, tempo_fechar: int = 3) -> dict:
    wa.sendwhatmsg_instantly(numero, msg, temp_espera, fecha_janela, tempo_fechar)
    return {"status": "Mensagem enviada com sucesso!"}