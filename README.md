# fastapi-boilerplate
A Fastapi boilerplate for backend dev
# Configuration for local development
1. create virtual environment
python3 -m venv venv
2. activate the environment 
  source ${pwd}/venv/bin/activate
4. create .env file and copy .env-example on it
5. intall dependencies
  pip install -r requirements.txt
6. start the server with uvicorn
  uvicorn app.main:app --reload
 - the server should be runing on 🍎 http://127.0.0.1:8000
# conf for docker environment
1.modify variables on docker-compose.yml then run 
  docker-compose up
 
Happy debugging :)


