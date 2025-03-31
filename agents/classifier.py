from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser

from app.config import OPENAI_API_KEY, LLM_MODEL
from models.schema import QueryClassification, Department

from langchain.output_parsers.format_instructions import PYDANTIC_FORMAT_INSTRUCTIONS

from utils.prompt_templates import Univeristy_Chatbot_Prompt


class QueryClassifier:
    def __init__(self):
        self.llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=LLM_MODEL,temperature=0.0)
        self.parser = PydanticOutputParser(pydantic_object=QueryClassification)

        format_instructions = self.parser.get_format_instructions()

        formatted_prompt = Univeristy_Chatbot_Prompt.format(format_instructions=format_instructions)

        self.prompt = ChatPromptTemplate.from_messages([
            ("system",formatted_prompt),
            ("human","{query}")
        ])

        self.chain = self.prompt | self.llm | self.parser

    def classify(self, query:str) -> QueryClassification:
        """
        Classify a user query to determine the appropriate department.
        :param query: User's query text
        :return: QueryClassification: Classification result with department and required info
        """

        try:
            return self.chain.invoke({"query":query})
        except Exception as e:
            return QueryClassification(
                department=Department.CSE,
                reason="Unable to fully understand the query",
                required_info={"more_details": "Please provide more specific information about your request"}
            )
