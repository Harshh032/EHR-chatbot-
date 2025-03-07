from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain_groq import ChatGroq
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
import re
import os
from dotenv import load_dotenv

load_dotenv()


memory = ConversationBufferMemory()

# NEO4J_URI='neo4j+s://635b0d32.databases.neo4j.io'
# NEO4J_USERNAME='neo4j'
# NEO4J_PASSWORD='yk103w56tQzrnFODPyVObTUd8zSYfTNHuEn35UKIFyI'



NEO4J_URI='neo4j+s://384416a4.databases.neo4j.io'
NEO4J_USERNAME='neo4j'
NEO4J_PASSWORD='TO1fnKfmAuLejQHiRJy2_ACDDSvIUUXB7m1_EmSJQAQ'
# os.getenv("GROQ_API_KEY" ,"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")
GROQ_API_KEY = os.getenv("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")

# GROQ_API_KEY = "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"
SIMPLE_GREETINGS = ["hi", "hello", "hey", "hi there", "hello there"]

def initialize_chatbot(graph):

    prompt = PromptTemplate(
        input_variables=["question", "context"],
        template=(
                "You are a healthcare assistant with access to patient data. "
                "Given the query: '{question}', and the following data: {context}, "
                "if user query is hii/hello than give them greetings how can i help you with finding patients. "
                "provide a human-readable response. For example, list patients with their names and details if applicable. Give response by thinking that you know the answer ie. you are giving the answer by yourself."
            ),
        )
    try:
        llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.3-70b-versatile", temperature=0.5)
        # llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)
        chain = GraphCypherQAChain.from_llm(
            llm=llm,
            graph=graph,
            qa_prompt=prompt,
            verbose=True,
            return_intermediate_steps=True, # for debugging
            allow_dangerous_requests=True
        )
        return chain
    except Exception as e:
        raise RuntimeError(f"Failed to initialize chatbot: {e}")
    


def generate_response(chain, prompt):
    try:

        if prompt.strip().lower() in SIMPLE_GREETINGS:
            return "Hi! How can I help you with finding patients?"
        
        memory.chat_memory.add_user_message(prompt)
        
        response = chain.invoke({"query": prompt,
                                 "history":memory.load_memory_variables({})})
        
        ai_reponse = response.get("result" , "No Response Returned")

        memory.chat_memory.add_ai_message(ai_reponse)

        intermediate_steps = response.get("intermediate_steps", [])
        for step in intermediate_steps:
            print(step)
            
        return response.get("result", "No response returned.")
    except Exception as e:
        return f"Error generating response: {e}"


def invokeChatbot(prompt):
    graph = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD) 
    chain = initialize_chatbot(graph)
    
    return generate_response(chain, prompt)
    

def main():
    # graph = Neo4jConnection(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)
    graph = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD) 

    try:

        chain = initialize_chatbot(graph)

        query = "Give patient information which medication has been completed?"
        response = generate_response(chain, query)
        print("Response:", response)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()