import asyncio
from swarm import Swarm, Agent

async def main():
    client = Swarm()

    english_agent = Agent(
        name="English Agent",
        instructions="You only speak English.",
    )

    spanish_agent = Agent(
        name="Spanish Agent",
        instructions="You only speak Spanish.",
    )

    def transfer_to_spanish_agent():
        """Transfer spanish speaking users immediately."""
        return spanish_agent

    english_agent.functions.append(transfer_to_spanish_agent)

    messages = [{"role": "user", "content": "Hola. ¿Como estás?"}]
    response = await client.run(agent=english_agent, messages=messages)

    print(response.messages[-1]["content"])

if __name__ == "__main__":
    asyncio.run(main())
