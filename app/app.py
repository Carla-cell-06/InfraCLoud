from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

DATA = "/data/messages.log"

TEMPLATE = """
<!doctype html>
<title>CloudEdu Services</title>
<h1>CloudEdu Services - Intranet</h1>
<p>Aplicación interna migrada a arquitectura cloud-native.</p>

<form method="POST">
  <input name="msg" placeholder="Escribe un mensaje interno" required>
  <button>Guardar</button>
</form>

<h3>Mensajes:</h3>
<pre>{{ logs }}</pre>
"""

def read_logs():
    if not os.path.exists(DATA):
        return ""
    with open(DATA, "r", encoding="utf-8") as f:
        return f.read()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        msg = request.form.get("msg", "").strip()
        if msg:
            os.makedirs("/data", exist_ok=True)
            with open(DATA, "a", encoding="utf-8") as f:
                f.write(msg + "\n")
    return render_template_string(TEMPLATE, logs=read_logs())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
