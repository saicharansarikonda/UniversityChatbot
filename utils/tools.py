from typing import Dict, Any, List, Callable
from langchain.agents import Tool

from models.schema import Department

class ToolRegistry:
    """Registry for all department tools."""

    def __init__(self):
        self.tools: Dict[Department, List[Tool]] = {
            Department.CSE:[],
            Department.LIBRARY:[],
            Department.ADMIN: [],
            Department.FINANCE: [],
            Department.SPORTS: [],
            Department.CAREER: [],
        }

    def register_tool(self, department:Department, name:str, func: Callable, description: str):
        """
        Register a new tool for a department.
        :param department: Department enum value
        :param name: name of the tool
        :param func: funciton to execute
        :param description: description of the tool including required/optional params
        """

        tool = Tool(
            name=name,
            func=func,
            description=description
        )
        self.tools[department].append(tool)


    def get_tools(self, department: Department):
        """
        Get all tools for a specific department
        :param department: department enum value
        :return: list of tools for the department
        """

        return self.tools[department]


    def get_all_tools(self):
        """
        get all tools from all departments
        :return: list of all tools
        """

        all_tools = []
        for dept_tools in self.tools.values():
            all_tools.extend(dept_tools)

        return all_tools

tool_registry = ToolRegistry()