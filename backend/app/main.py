from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return({"message":"Resume copilot API is running"})