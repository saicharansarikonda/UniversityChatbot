import json
import requests
from langchain.agents import Tool
from models.schema import Department
from utils.tools import tool_registry

# Base URL for your API
BASE_URL = "http://localhost:8000"

def handle_api_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"API request failed: {str(e)}"}

# Register all tools for all departments
def register_all_tools():
    print("Registering all department tools...")

    tool_registry.register_tool(
        department=Department.CSE,
        name="cse_course_info",
        func=handle_api_request,
        description=f"Get information about a specific course. Required: A full API URL like '{BASE_URL}/cse/course?course_code=CS101&semester=Spring%202024'."
    )

    tool_registry.register_tool(
        department=Department.CSE,
        name="cse_professor_info",
        func=handle_api_request,
        description=f"Get information about professors. Required: A full API URL like '{BASE_URL}/cse/professor?professor_name=Dr.%20Smith'."
    )

    print("Tool registration summary:")
    for dept, tools in tool_registry.tools.items():
        print(f"{dept.value}: {len(tools)} tools registered")
        for tool in tools:
            print(f"  - {tool.name}")

register_all_tools()