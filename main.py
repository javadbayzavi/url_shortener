from uvicorn import run 
from api.api import create_app
from core.environment import SERVER_HOST, SERVER_PORT



if __name__ == "__main__":
    run(app=create_app(), host=SERVER_HOST, port=SERVER_PORT)