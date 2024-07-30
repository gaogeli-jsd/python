# コルーチン(async, await)
# Python 3.5 で導入された機能で、関数を非同期に呼び出すことが可能となります。
# getsize() というコルーチンをタスクリストとして複数呼び出すことにより、
# 指定したURLのサイズを求めるというタスクを並列実行することができます。

# Python 3.5～
import asyncio
import requests

urls = [
    "https://www.yahoo.co.jp",
    "https://www.google.com",
    "https://www.wikipedia.com"
]

async def getsize(url):
    print(f"getsize({url}) START")
    loop = asyncio.get_event_loop()
    r = await loop.run_in_executor(None, requests.get, url)
    print(f"getsize({url}) END {len(r.text)} bytes")

async def main():
    print('main() START')
    tasks = [asyncio.create_task(getsize(url)) for url in urls]
    await asyncio.gather(*tasks)
    print('main() END')

if __name__ == "__main__":
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(main())

# Python 3.7 からは get_event_loop(), 
# run_until_complete() の代わりに run() を使用できるようになりました。
# Python 3.10 からは get_event_loop() が
# 非推奨となっているのでこちらを使用するのがよさそうです。
# Python 3.7～
    loop = asyncio.run(main())

'''
実行結果
main() START
getsize(https://www.yahoo.co.jp) START                 # getsize()が並列に呼び出されている
getsize(https://www.google.com) START                  #    〃
getsize(https://www.wikipedia.com) START               #    〃
getsize(https://www.yahoo.co.jp) END 35804 bytes
getsize(https://www.google.com) END 15135 bytes
getsize(https://www.wikipedia.com) END 75189 bytes
main() END
'''