from fastapi import status

from app import get_app

app = get_app()


@app.get("/", status_code=status.HTTP_200_OK, response_model=dict)
async def health_check():
    return {"status": "ok"}
