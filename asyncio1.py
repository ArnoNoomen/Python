import asyncio

async def fetch_data(max):
    for i in range(max):
        pass
    #    print(f'fetchdata {i}')
    return {'data': max}

async def print_number(max):
    for i in range(max):
        pass
        print(f'print_number {i} {max}')
    #print(max)

async def main():
    taks1 = asyncio.create_task(fetch_data(200))
    taks2 = asyncio.create_task(fetch_data(100))
    print('start task3')    
    taks3 = asyncio.create_task(print_number(100000))
    print('start task4')
    taks4 = asyncio.create_task(print_number(200000))
    print('Hallo')
    value1 = await(taks1)
    print(value1)
    value2 = await(taks2)
    print(value2)

    # Schedule three calls *concurrently*:
    await asyncio.gather(
        print_number(100000),
        print_number(2000),
        print_number(30000),
    )
    
if __name__ == '__main__':
    asyncio.run(main())