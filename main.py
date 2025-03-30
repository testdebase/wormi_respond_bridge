from fastapi import FastAPI, Request
import requests

app = FastAPI()

LOCAL_SERVER_URL = "http://<TON_IP_LOCALE>:8000/respond"  # à remplacer !

@app.post("/respond")
async def respond(request: Request):
    body = await request.json()
    try:
        resp = requests.post(LOCAL_SERVER_URL, json=body)
        print(f"[Forwarded] Requête renvoyée à ta machine locale - status {resp.status_code}")
        return {"status": "forwarded", "code": resp.status_code}
    except Exception as e:
        print(f"[Error] Impossible de contacter ton serveur local : {e}")
        return {"error": str(e)}
