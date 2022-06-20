sudo apt update

# 安装ruby
sudo apt install -y ruby

# 安装RubyGems
sudo apt install -y rubygems

# 利用gem安装jeykll
gem install -y jekyll

# 安装net-tools，以便于使用ping
sudo apt update &&  sudo apt install -y iproute2
sudo apt install -y iputils-ping
sudo apt-get install net-tools 
