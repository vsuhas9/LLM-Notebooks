"""
 * author Suhas V
 * created on 16-09-2024-23h-36m
"""


from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# _logger = logging.get_logger(__file__)

__all__ = [
    "GetModels"
]


class GetModels:
    R""" Class to handle model creation
    """

    def __init__(self) -> None:
        R""" Creates an object of the class 'GetModels'
        """
        self.llm = ChatOllama(
            model="llama3.1",
            temperature=0,
            keep_alive=True
        )

        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful chat assistant which is capable of answering user questions"
                ),
                (
                    "human",
                    "question: {input}"
                )
            ]
        )

    def get_llm(self):
        R""" Methods to return the llm model
        """
        return self.llm

    def get_chain(self):
        R""" Method to return a llm chain
        """
        return self.prompt | self.llm

    def invoke_chain(self, query):
        R""" Method to invoke a llm
        """
        chain = self.get_chain()

        response = chain.invoke({
            "input": query
        })
        return response
