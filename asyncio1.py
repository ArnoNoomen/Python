import asyncio

async def fetch_data(maxa):
    for _i in range(maxa):
        pass
    return {'data': maxa}

async def print_number(maxa):
    for i in range(maxa):
        print(f'print_number {i} {maxa}')
    print(maxa)

async def main():
    task1 = asyncio.create_task(fetch_data(200))
    task2 = asyncio.create_task(fetch_data(100))
    print('start task3')
    task3 = asyncio.create_task(print_number(10))
    print('start task4')
    task4 = asyncio.create_task(print_number(20))
    print('Hallo')
    value1 = await(task1)
    print(value1)
    value2 = await(task2)
    print(value2)

    #Schedule three calls *concurrently*:
    await asyncio.gather(
        print_number(50),
        print_number(60),
        print_number(70),
    )


if __name__ == '__main__':
    asyncio.run(main())
