# demo-03, generator usage

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None) # start generator
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # change to consumer
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()

produce(c)