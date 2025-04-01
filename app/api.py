import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.schema import ChatRequest, ChatResponse
from agents.chatbot import chatbot


from departments.cse import routes as cse_routes
from departments.admin import routes as admin_routes
from departments.finance import routes as finance_routes
from departments.library import routes as library_routes
from departments.sports import routes as sports_routes
from departments.career import routes as career_routes

app = FastAPI(
    title="University Chatbot API",
    description="API for a university chatbot with department specific agents"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cse_routes.router)
app.include_router(admin_routes.router)
app.include_router(finance_routes.router)
app.include_router(library_routes.router)
app.include_router(sports_routes.router)
app.include_router(career_routes.router)

@app.post("/chat",response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    process a chat query and get a response from the appropriate department
    :param request: ChatRequest object with user query
    :return: ChatResponse with the chatbot's response
    """
    try:
        response = await chatbot.process_query(request.query)
        return response
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

