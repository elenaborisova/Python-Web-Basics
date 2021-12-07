from urllib.parse import unquote


def decode(encoded_url):
    return unquote(encoded_url)


print(decode('http://www.google.bg/search?q=C%23'))
print(decode('https://mysite.com/show?n%40m3=p3%24h0'))
print(decode('http://url-decoder.com/i%23de%25?id=23'))