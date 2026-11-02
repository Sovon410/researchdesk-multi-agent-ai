from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS

from backend.teams import ResearchTeam


app = Flask(__name__)
CORS(app)

team = ResearchTeam().research_team()



@app.get("/api/health")
def health():
    return jsonify({"status" : "ok"})


@app.post("/api/chat")
def chat():
    data = request.get_json(silent= True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"error" : "message is required"}), 400
    
    try:
        result = team.run(message)
        return jsonify({"reply" : result.content})
    except Exception as e:
        return jsonify({"error" : str(e)}), 500


@app.post("/api/chat/stream")
def chat_stream():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"error": "message is required"}), 400

    def generate():
        for chunk in team.run(message, stream=True):
            if getattr(chunk, "content", None):
                yield chunk.content

    return Response(stream_with_context(generate()), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host= "127.0.0.1", port= 5000, debug= False, threaded= True)