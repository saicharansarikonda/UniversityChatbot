from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

from app.config import OPENAI_API_KEY, LLM_MODEL
from models.schema import Department
from utils.prompt_templates import Department_Chatbot_Prompt
from utils.tools import tool_registry

class DepartmentAgent:
    """
    Agent for handling department-specific queries.
    """

    def __init__(self,department: Department):
        """
        Initialize a department agent
        :param department: the department this agent handles
        """

        self.department = department
        self.llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=LLM_MODEL,temperature=0.0)
        self.tools = tool_registry.get_tools(department)
        self.memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
        system_prompt = Department_Chatbot_Prompt.get(department.value)

        self.prompt = ChatPromptTemplate.from_messages([
            ("system",system_prompt),
            ("human","{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])


        agent = create_openai_functions_agent(self.llm, self.tools, self.prompt)
        self.executor = AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=self.tools,
            memory=self.memory,
            verbose=True
        )


    async def process_query(self, query:str) -> str:
        """
        process a user query and return a response.
        :param query: user's query text
        :return: response text from the agent
        """
        response = await self.executor.ainvoke({"input":query})
        return response["output"]