from . app import load_questao
# 
app = FastApi()

@app.get("/questoes"):
  return load_data()