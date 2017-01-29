echo "BEFORE INSTALL"
echo 'killing existing flask process'
ps -ef | grep flask | grep -v grep | awk '{print $2}' | xargs kill
sleep 10
echo "Removing old application bundle"
rm -rf /home/ec2-user/flaskr
