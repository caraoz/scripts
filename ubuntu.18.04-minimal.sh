## set up basic packages for minimal install
apt update;
apt install tmux pv nload htop git iotop curl ntpdate nethogs nmap ;

## sync time to prevent future update errors
ntpdate 1.ro.pool.ntp.org;

## install python modules
apt install python3-pip;
pip3 install youtube-dl BeautifulSoup4 schedule;
