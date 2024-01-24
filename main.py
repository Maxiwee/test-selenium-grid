from flask import Flask, request
from controllers.queue import Queue

app = Flask(__name__)
queue = Queue()


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/test')
def asd():
    body = request.json
    queue_start = queue.start_thread(body["name"])
    return queue_start


@app.route('/queues')
def queues():
    a = queue.queue
    return a


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3005, debug=False)
    #urls = ["https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/", "https://dev.viradoctores.com/"]

    #hilos = []
    #c = 1
    #for url in urls:
    #    thread = threading.Thread(target=test, args=(url, c))
    #    c +=1
    #    hilos.append(thread)
    #    thread.start()

    #for hilo in hilos:
    #    hilo.join()

    #with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #    results = list(executor.map(test, urls))

    #for url in urls:
    #    test(url)

    #for res in results:
        #print(res)
