import asyncio
from nats.aio.client import Client as NATS

async def main():
    # Connect to the NATS server
    nc = NATS()
    await nc.connect("nats://localhost:4222")

    # Publish a message to the "my_subject" subject
    message = "Hello, NATS!"
    await nc.publish("my_subject", message.encode())

    # Disconnect from the NATS server
    await nc.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())