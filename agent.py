import asyncio
from mcp_agent.core.fastagent import FastAgent

# Declare FastAgent Application
fast = FastAgent("MultiTool Assistant")

# Define a single agent with access to multiple servers
description = """
You are a helpful assistant. You may use math or weather tools to answer user queries.
"""

@fast.agent(
    name="assistant",
    instruction=description,
    servers=["math", "weather", "playwright"]
)
async def main():
    async with fast.run() as agent:
        await agent.interactive()

if __name__ == "__main__":
    asyncio.run(main())