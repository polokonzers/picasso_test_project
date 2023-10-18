from celery import Celery

app = Celery('picasso_test_project',
             broker='amqp://',
             backend='rpc://',
             include=['picasso_test_project.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
