from celery import Celery
import os
import logging 

broker_url = os.environ.get('CLOUDAMQP_URL')
app = Celery('tasks', backend='rpc://', broker="amqp://tulhovxu:QawaE4c2HcT64tmi4KiemLumAxh_d4Xz@hawk.rmq.cloudamqp.com/tulhovxu")

@app.task(name='vector.tasks.say')
def vector_say(message):
    #logging.debug('Making Vector say: %s' % message)
    print(message)
    # say = VectorSay()
    # await say.perform(message)
    
    
if __name__ == '__main__':
    app.start()