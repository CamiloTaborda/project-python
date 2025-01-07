import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def getList():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def getContact():
    return """
      <h1>Soy un titulo</h1>
      <p>Soy un texto</p>
    """


def run():
    store.getCategories()

if __name__=='__main__':
    run()    
