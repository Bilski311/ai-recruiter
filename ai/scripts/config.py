import os 

CHAT_TEMPERATURE = 0
MONGO_URI = os.environ['MONGO_URI']
MONGO_DB = "ai_recruiter"
MONGO_COLLECTION = "generated_content"
SAVE_TO_MONGO = False
BACKEND_URL = "http://localhost:5000/"
