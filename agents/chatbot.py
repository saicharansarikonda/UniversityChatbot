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


    async def process_query(self,query:str) -> ChatResponse:
        """
        process a user query and return a response
        :param query: user's query text
        :return: ChatResponse object with response data
        """

        try:
            classification = self.classifier.classify(query)
            department = classification.department
            required_info = classification.required_info

            missing_info = {}
            for tool in self.department_agents[department].tools:
                tool_name = tool.name

                required_params = []

                if "Required:" in tool.description:
                    required_part = tool.description.split("Required:")[1].split(".")[0]
                    required_params = [param.strip() for param in required_part.split(",")]

                if tool_name.split("_")[0] in department.value.lower().split()[0]:
                    for param in required_params:
                        if param not in required_info or not required_info[param]:
                            missing_info[param] = f"Please provide the {param}"


            if missing_info:
                return ChatResponse(
                    department=department.value,
                    status="need_more_info",
                    required_info=missing_info
                )

            response = await self.department_agents[department].process_query(query)

            return ChatResponse(
                department=department.value,
                status="success",
                response=response,
                used_info=required_info
            )

        except Exception as e:
            return ChatResponse(
                department=department.value,
                status="error",
                message = str(e)
            )

chatbot = UniversityChatbot()