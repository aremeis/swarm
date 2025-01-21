import asyncio
from swarm import Swarm, Agent

async def main():
    client = Swarm()

    def get_weather(location) -> str:
        return "{'temp':67, 'unit':'F'}"

    agent = Agent(
        name="Agent",
        instructions="You are a helpful agent.",
        functions=[get_weather],
    )

    messages = [{"role": "user", "content": "What's the weather in NYC?"}]

    response = await client.run(agent=agent, messages=messages)
    print(response.messages[-1]["content"])

if __name__ == "__main__":
    asyncio.run(main())
