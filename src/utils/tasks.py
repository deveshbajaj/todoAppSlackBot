from celery import Celery 
import sys
sys.path.insert(0,'/code/utils/')
import userLogs
from datetime import datetime
app = Celery ('tasks', backend='redis://redis', broker='redis://redis')

@app.task(name='utils.tasks.add_logged_user')
def add_logged_user(login_data):
    print('devesh bajaj',login_data)
    current_time = str(datetime.now())
    just_logged_user = userLogs.UserLogs(
        user_name=login_data['user_name'],
        mongo_id=login_data['mongo_id'],
        timestamp=current_time
        ).save()
    return(just_logged_user.to_json())


if __name__ == '__main__':
    # log stuff about the configuration
    app.conf.enable_utc = True
    app.worker_main()
