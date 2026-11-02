import uvicorn

from projectback.setup import app

if __name__ == "__main__":
    uvicorn.run(app)

    