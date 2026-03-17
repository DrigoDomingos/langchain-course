import logging
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

load_dotenv()

# Configure logging with ERROR level
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def main():
    logger.error("Hello from langchain-course!")
    information = "Elon Musk is a business magnate and investor known for his work in the technology and space industries. He is the CEO of SpaceX and Tesla, Inc., and has been involved in various other ventures such as Neuralink and The Boring Company. Musk is recognized for his ambitious goals, including colonizing Mars and advancing sustainable energy solutions. He has also made significant contributions to the development of electric vehicles and space exploration technologies."
    summary_template= """
    given the information {information} about a person I want you to write a short summary about this person. The summary should be concise and highlight the key aspects of the person's life, achievements, and characteristics. Please ensure that the summary is well-structured and provides a clear overview of the individual's background and significance.
    1 - a short summary about the person should be provided in the output.
    2 - the summary should be concise and highlight the key aspects of the person's life,
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    #llm = ChatOllama(model="gemma3:270m", temperature=0, base_url="http://localhost:11434")

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)



if __name__ == "__main__":
    main()
