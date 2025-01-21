import asyncio
from swarm import Swarm, Agent

async def pretty_print_messages(messages):
    for message in messages:
        if message["content"] is None:
            continue
        print(f"{message['sender']}: {message['content']}")

async def main():
    client = Swarm()

    my_agent = Agent(
        name="Agent",
        instructions="You are a helpful agent.",
    )

    messages = []
    agent = my_agent
    while True:
        user_input = input("> ")
        messages.append({"role": "user", "content": user_input})

        response = await client.run(agent=agent, messages=messages)
        messages = response.messages
        agent = response.agent
        await pretty_print_messages(messages)

if __name__ == "__main__":
    asyncio.run(main())
