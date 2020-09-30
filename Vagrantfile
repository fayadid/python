Vagrant.configure("2") do |config|
  config.vm.box = "fayadid/training-centos"
  config.vm.box_version = "0.0.1"
  config.vm.hostname = "PythonCentos"
  config.vm.provider :virtualbox do |vb|
            vb.name = "PythonCentos"
  end
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.synced_folder "Python/", "/home/vagrant/Python/", automount:true
end