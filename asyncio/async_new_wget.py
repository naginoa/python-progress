import asyncio


async def wget(host):
    print('wget %s...' % host)
    conn = asyncio.open_connection(host, 80)
    reader, writer = await conn
    header = 'GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
#请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
#把@asyncio.coroutine替换为async；
#把yield from替换为await。