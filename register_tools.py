"""
Centralized place to register all tools for the chatbot.
This module should be imported early in the application startup.
"""
import json
import ast
import requests
from langchain.agents import Tool
from models.schema import Department
from utils.tools import tool_registry

# Base URL for your API
BASE_URL = "http://localhost:8000"  # Change this to match your server configuration

# Function to handle course info requests via API
def handle_course_info(args_str):
    # Check if the argument is just a simple string (like "CS101")
    if args_str.strip('"\'').isalnum() and not args_str.startswith('{'):
        # If it's just a course code string, use it directly
        course_code = args_str.strip('\'"')
        url = f"{BASE_URL}/cse/course?course_code={course_code}"
    else:
        # Parse as dictionary
        args = parse_args(args_str)

        # Build URL with parameters
        url = f"{BASE_URL}/cse/course?course_code={args.get('course_code', '')}"
        if 'semester' in args and args['semester']:
            url += f"&semester={args['semester']}"

    # Make the API request
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for non-200 status codes
        return response.json()
    except Exception as e:
        return {"error": f"API request failed: {str(e)}"}

# Function to handle professor info requests via API
# Function to handle professor info requests via API
def handle_professor_info(args_str):
    # If args_str is empty or just whitespace, make a request with no parameters
    if not args_str or args_str.strip() == '{}' or args_str.strip() == '':
        url = f"{BASE_URL}/cse/professor"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"API request failed: {str(e)}"}

    # Otherwise, parse arguments as before
    args = parse_args(args_str)

    # Build URL with parameters
    url = f"{BASE_URL}/cse/professor"
    params = {}

    if 'professor_name' in args:
        params['professor_name'] = args['professor_name']
    if 'department' in args:
        params['department'] = args['department']

    # Make the API request
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"API request failed: {str(e)}"}

# Helper function for safely parsing arguments
def parse_args(args_str):
    try:
        # First try to parse as JSON
        return json.loads(args_str)
    except:
        try:
            # Try the safer ast.literal_eval
            return ast.literal_eval(args_str)
        except:
            # If both fail, use a simple manual approach
            args_dict = {}
            # Remove braces
            clean_str = args_str.strip('{}')
            # Split by commas
            parts = clean_str.split(',')

            for part in parts:
                if ':' in part:
                    key, value = part.split(':', 1)
                    # Clean up the key and value
                    key = key.strip().strip('\'"')
                    value = value.strip().strip('\'"')
                    args_dict[key] = value

            return args_dict

# Register all tools for all departments
def register_all_tools():
    print("Registering all department tools...")

    # Register CSE tools using API handlers
    tool_registry.register_tool(
        department=Department.CSE,
        name="cse_course_info",
        func=handle_course_info,
        description="Get information about a specific course. Required: course_code. Optional: semester."
    )

    tool_registry.register_tool(
        department=Department.CSE,
        name="cse_professor_info",
        func=handle_professor_info,
        description="Get information about professors. Optional: professor_name, department."
    )

    # Check registration
    print("Tool registration summary:")
    for dept, tools in tool_registry.tools.items():
        print(f"{dept.value}: {len(tools)} tools registered")
        for tool in tools:
            print(f"  - {tool.name}")

# Register tools immediately when this module is imported
register_all_tools()