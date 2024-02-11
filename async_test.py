import asyncio
import time

async def call_sleep(t):
  print("init: ", t)
  await asyncio.sleep(t)
  print("done ",t)  
  return t*t

async def main():
  # t1 = asyncio.create_task(call_sleep(1))
  # t2 = asyncio.create_task(call_sleep(2))
  # t3 = asyncio.create_task(call_sleep(3))

  t = [asyncio.create_task(call_sleep(t)) for t in range(1,10)]

  results = await asyncio.gather(*t)
  print(*results, sep="\n")
  print("done all")

if __name__ == "__main__":
  asyncio.run(main())