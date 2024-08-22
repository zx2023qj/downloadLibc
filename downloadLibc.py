import requests
import json


def downloadLibc(symbols, address):
    response = requests.post(url=url, json={"symbols": {symbols: address}})
    response = json.loads(response.text)
    for item in response:
        res = requests.get(url=item['download_url'])
        if res.status_code == 200:
            # 以二进制写入模式打开本地文件
            with open(item['id'] + '.so', "wb") as file:
                # 分块写入文件内容
                for chunk in res.iter_content(chunk_size=8192):
                    file.write(chunk)
            print("文件下载成功")
        else:
            print(f"文件下载失败，状态码：{res.status_code}")


def downloadLibcSymbols(symbols, address):
    response = requests.post(url=url, json={"symbols": {symbols: address}})
    response = json.loads(response.text)
    for item in response:
        res = requests.get(url=item['symbols_url'])
        if res.status_code == 200:
            # 以二进制写入模式打开本地文件
            with open(item['id'] + '.symbols', "wb") as file:
                # 分块写入文件内容
                for chunk in res.iter_content(chunk_size=8192):
                    file.write(chunk)
            print("文件下载成功")
        else:
            print(f"文件下载失败，状态码：{res.status_code}")


def downloadLibcDeb(symbols, address):
    response = requests.post(url=url, json={"symbols": {symbols: address}})
    response = json.loads(response.text)
    for item in response:
        print(item)
        res = requests.get(url=item['libs_url'])
        if res.status_code == 200:
            # 以二进制写入模式打开本地文件
            with open(item['id'] + '.deb', "wb") as file:
                # 分块写入文件内容
                for chunk in res.iter_content(chunk_size=8192):
                    file.write(chunk)
            print("文件下载成功")
        else:
            print(f"文件下载失败，状态码：{res.status_code}")


if __name__ == '__main__':
    url = "https://libc.rip/api/find"
    symbols = input("** symbols:   ")
    address = input("** address(prefix:0x):   ")
    downloadLibc(symbols, address)
    downloadLibcSymbols(symbols,address)
    downloadLibcDeb(symbols,address)
