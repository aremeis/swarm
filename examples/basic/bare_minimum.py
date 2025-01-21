import asyncio
from swarm import Swarm, Agent

async def main():
    client = Swarm()

    agent = Agent(
        name="Agent",
        instructions="You are a helpful agent.",
    )

    messages = [{"role": "user", "content": "Hi!"}]
    response = await client.run(agent=agent, messages=messages)

    print(response.messages[-1]["content"])

if __name__ == "__main__":
    asyncio.run(main())
