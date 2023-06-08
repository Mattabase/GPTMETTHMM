'''
THE PROGRAM USES SEVERAL APIS LIKE FOLLOWS WHOSE SOURCE CODE IS CURRENTLY NOT DISCLOSED SO THAT THESE API MAY NOT GET PATCHED
CREDITS & CITATIONS:
https://github.com/acheong08/EdgeGPT/
https://gitler.moe/g4f/gpt4free
'''

#-----------------DEMO CODE-----------------

import asyncio
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
import json

async def main():
    cookies = json.loads(open(r"cookies.json", encoding="utf-8").read())  # might omit cookies option
    bot = await Chatbot.create(cookies=cookies) # Passing cookies is "optional", as explained above
    print(await bot.ask(prompt="Hello world", conversation_style=ConversationStyle.creative))
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())

#-----------------DEMO CODE-----------------
