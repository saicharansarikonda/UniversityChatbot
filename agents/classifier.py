from typing import Optional, Dict, Any

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser

from app.config import OPENAI_API_KEY, LLM_MODEL
from models.schema import QueryClassification, Department

from utils.prompt_templates import University_Chatbot_Prompt


class QueryClassifier:
    def __init__(self):
        self.llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=LLM_MODEL, temperature=0.0)

        self.parser = PydanticOutputParser(pydantic_object=QueryClassification)

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", University_Chatbot_Prompt),
            ("human", "{query}\n{format_instructions}")
        ])

        self.chain = self.prompt | self.llm | self.parser

    def classify(self, query: str) -> Optional[QueryClassification]:
        """
        Classify a user query to determine the appropriate department.
        :param query: User's query text
        :return: QueryClassification or None if classification fails
        """
        try:
            return self.chain.invoke({
                "query": query,
                "format_instructions": self.parser.get_format_instructions()
            })
        except Exception as e:
            print(f"Classification error: {str(e)}")
            return None