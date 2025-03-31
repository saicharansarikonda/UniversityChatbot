from typing import Dict, Any
import asyncio

from models.schema import Department, ChatResponse
from agents.classifier import QueryClassifier
from agents.department_agent import DepartmentAgent

class UniversityChatbot:
    def __init__(self):
        self.classifier = QueryClassifier()
        self.department_agents = {
            Department.CSE: DepartmentAgent(Department.CSE),
            Department.LIBRARY : DepartmentAgent(Department.LIBRARY),
            Department.ADMIN: DepartmentAgent(Department.ADMIN),
            Department.FINANCE: DepartmentAgent(Department.FINANCE),
            Department.SPORTS: DepartmentAgent(Department.SPORTS),
            Department.CAREER: DepartmentAgent(Department.CAREER),
        }

    async def process_query(self, query: str) -> ChatResponse:
        """
        Process a user query and return a response
        :param query: user's query text
        :return: ChatResponse object with response data
        """
        try:
            classification = self.classifier.classify(query)

            if classification is None:
                return ChatResponse(
                    status="error",
                    message="I'm sorry, I couldn't understand what department your query relates to. Could you please rephrase your question or provide more details?"
                )

            department = classification.department
            response = await self.department_agents[department].process_query(query)

            return ChatResponse(
                department=department.value,
                status="success",
                response=response
            )

        except Exception as e:
            return ChatResponse(
                status="error",
                message=str(e)
            )

chatbot = UniversityChatbot()