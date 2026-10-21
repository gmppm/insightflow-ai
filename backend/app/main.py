from fastapi import FastAPI


app = FastAPI(
    title="InsightFlow AI API",
    description="Backend API for InsightFlow AI",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}