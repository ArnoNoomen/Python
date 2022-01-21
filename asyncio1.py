import asyncio

async def fetch_data(max):
    for i in range(max):
        print(f'fetchdata {i}')
    return {'data': max}

async def print_number():
    for i in range(100):
        print(f'print_number {i}')

async def main():
    taks1 = asyncio.create_task(fetch_data(200))
    taks2 = asyncio.create_task(fetch_data(100))
    taks3 = asyncio.create_task(print_number())
    taks4 = asyncio.create_task(print_number())
    print('Hallo')
    value1 = await(taks1)
    print(value1)
    value2 = await(taks2)
    print(value2)

if __name__ == '__main__':
    asyncio.run(main())