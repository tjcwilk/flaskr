echo "Application start"
export PATH=$PATH:/usr/local/bin
export PYTHONPATH=$PYTHONPATH:/usr/local/bin
cd /home/ec2-user/flaskr 
export FLASK_APP=flaskr 
flask initdb
flask run --host=0.0.0.0 --port=80 > /dev/null 2>&1 &
