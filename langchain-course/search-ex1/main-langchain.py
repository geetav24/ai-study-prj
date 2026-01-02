from dotenv import load_dotenv
load_dotenv()
import os
import sys
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

tavily = TavilySearch()


def main():
    print("Hello from langchain-course!")

    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("ERROR: OPENAI_API_KEY not found in environment.")
        print("- Activate your virtualenv:")
        print("  source /Users/geeta-mit/study/ai-study/udemy/langchain-course/.venv/bin/activate")
        print("- Set the environment variable (one-time):")
        print("  export OPENAI_API_KEY=\"sk-...\"")
        print("Or create a `.env` file in the project root with a line: OPENAI_API_KEY=sk-...")
        sys.exit(1)

    print(f"Using OpenAI API key (first 6 chars): {key[:6]}...")

    # Create the LLM and agent after we've verified the environment
    llm = ChatOpenAI()
    tools = [tavily]
    agent = create_agent(llm,tools)
   
    # Use the higher-level initialize_agent helper which handles prompts internally
    try:
        # agent_executor = initialize_agent(
        #     tools=tools,
        #     llm=llm,
        #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        #     verbose=False,
        # )
       response = agent.invoke({"messages" : HumanMessage(content="What is the weather in Tokyo?")})
       print(f"Agent response: {response}")
    except TypeError:
        # Fallback: older/newer langchain versions may accept different arg order
         print(f"Error")
      
      


if __name__ == "__main__":
    main()
