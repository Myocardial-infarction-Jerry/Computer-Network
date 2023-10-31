sudo iptables -A DOCKER-USER -i docker0 -s 172.17.0.4/32 -d 172.17.0.2/32 -m time --timestart 09:00 --timestop 17:00 --weekdays Mon,Tue,Wed,Thu,Fri --kerneltz -j ACCEPT
sudo iptables -A DOCKER-USER -i docker0 -s 172.17.0.4/32 -d 172.17.0.3/32 -m time --timestart 09:00 --timestop 17:00 --weekdays Mon,Tue,Wed,Thu,Fri --kerneltz -j DROP
sudo iptables -A DOCKER-USER -i docker0 -s 172.17.0.4/32 -d 172.17.0.2/32 -m time --timestart 17:00 --timestop 09:00 --weekdays Mon,Tue,Wed,Thu,Fri --kerneltz -j DROP
sudo iptables -A DOCKER-USER -i docker0 -s 172.17.0.4/32 -d 172.17.0.3/32 -m time --timestart 17:00 --timestop 09:00 --weekdays Mon,Tue,Wed,Thu,Fri --kerneltz -j ACCEPT
sudo iptables -A DOCKER-USER -i docker0 -s 0.0.0.0/0 -d 0.0.0.0/0 -j RETURN
