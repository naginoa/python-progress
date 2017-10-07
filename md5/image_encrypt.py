import hashlib


#md5
with open('test.jpg', 'rb') as f:
    hash = hashlib.md5()
    old = f.read()
    print('二进制图片内容：' ,old)
    hash.update(bytes(str(f.read())[2:-2], encoding='utf-8'))
    print('md5加密后的字符串为：',hash.hexdigest())
    print('md5加密后的二进制串为：',hash.digest())
    with open('test_md5.jpg', 'wb') as f:
        f.write(hash.digest())
    md5_decode = old
    with open('test_md5_decode.jpg', 'wb') as f:
        f.write(md5_decode)


#sha1
with open('test.jpg', 'rb') as f:
    hash = hashlib.sha1()
    old = f.read()
    print('二进制图片内容：' ,old)
    hash.update(bytes(str(f.read())[2:-2], encoding='utf-8'))
    print('sha1加密后的字符串为：',hash.hexdigest())
    print('sha1加密后的二进制串为：',hash.digest())
    with open('test_sha1.jpg', 'wb') as f:
        f.write(hash.digest())
    md5_decode = old
    with open('test_sha1_decode.jpg', 'wb') as f:
        f.write(md5_decode)