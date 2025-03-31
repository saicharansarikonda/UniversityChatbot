from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser

from app.config import OPENAI_API_KEY, LLM_MODEL
from models.schema import  QueryClassification

from utils.prompt_templates import Univeristy_Chatbot_Prompt


class QueryClassifier:
    def __init__(self):
        self.llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=LLM_MODEL)
        self.parser = PydanticOutputParser(pydantic_object=QueryClassification)

        self.prompt = ChatPromptTemplate.from_messages([
            ("system",Univeristy_Chatbot_Prompt),
            ("human","{query}")
        ])

        self.chain = self.prompt | self.llm | self.parser

    def classify(self, query:str) -> QueryClassification:
        """
        Classify a user query to determine the appropriate department.
        :param query: User's query text
        :return: QueryClassification: Classification result with department and required info
        """

        return self.chain.invoke({"query":query})
