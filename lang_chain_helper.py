import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Load API key from .env file
load_dotenv()
openai_api_key = os.getenv("API_KEY")

# Initialize the OpenAI LLM
llm = OpenAI(temperature=0.6, openai_api_key=openai_api_key)

def generate_restaurant_name_items(cusine):
    # Step 1: Create the prompt template for the restaurant name
    Prompt_Template_name = PromptTemplate(
        input_variables=["cusine"],
        template="Give me only one restaurant name for {cusine} food."
    )

    # Step 2: Create the prompt template for the menu
    Prompt_Template_menu = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Give me 5 menu items for {restaurant_name} without discriptions."
    )

    # Step 3: Create LLM chains
    name_chain = LLMChain(llm=llm, prompt=Prompt_Template_name, output_key="restaurant_name")
    menu_chain = LLMChain(llm=llm, prompt=Prompt_Template_menu, output_key="menu")

    # Step 4: Combine them using SequentialChain
    sequential_chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=["cusine"],  # Inputs to the first chain
        output_variables=["restaurant_name","menu"],  # Outputs from the final chain
        verbose=True
    )

    # Step 5: Run the chain with invoke
    response = sequential_chain.invoke({"cusine": cusine})
    return response

