import asyncio
from nats.aio.client import Client as NATS

async def message_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    print(f"Received a message on '{subject}': {data}")

async def main():
    # Connect to the NATS server
    nc = NATS()
    await nc.connect("nats://localhost:4222")

    # Subscribe to a subject
    await nc.subscribe("my_subject", cb=message_handler)

    # Keep the client running to receive messages
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass

    # Disconnect from the NATS server
    await nc.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
