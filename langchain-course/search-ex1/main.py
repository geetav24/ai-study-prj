from dotenv import load_dotenv
load_dotenv()
import os
import sys
from langchain.agents import initialize_agent, AgentExecutor, AgentType
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage

@tool
def search_tool(query: str) -> str:
    """    
    Tool that searches over the internet
    Args:
        query (str): The search query
    Returns:
        str: The search results
    """
    print(f"Searching for: {query}")
    return "Tokyo weather is sunny"

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
    tools = [search_tool]

    # Use the higher-level initialize_agent helper which handles prompts internally
    try:
        agent_executor = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False,
        )
    except TypeError:
        # Fallback: older/newer langchain versions may accept different arg order
        agent_executor = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)

    response = agent_executor.run("What is the weather in Tokyo?")
    print(f"Agent response: {response}")


if __name__ == "__main__":
    main()
