# demo-03, generator basic usage.
# a simple Producer-consumer demo

def consumer(): # a generator
    r = ''
    while True:
        n = yield r # 4.each call start from here
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None) # 1.start generator, pass outside value to generator inner
    n = 0
    while n < 5:
        n = n + 1 # 2.begin to produce
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # 3.change to consumer
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()

produce(c)