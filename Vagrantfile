Vagrant.configure('2') do |config|
  config.vm.box = "bento/ubuntu-19.10"

    # use local ssh key to connect to remote vagrant box
    config.ssh.private_key_path = '~/.ssh/id_rsa'
 
    # Evitar que busque actualizaciones
    config.vm.box_check_update = false

    # configuramos la red de nuestra máquina
    config.vm.network "forwarded_port", guest: 8000, host: 8000


  end

  # Configuración  para provisionar con ansible
    config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.version = "2.7.5"
    ansible.playbook = "provision/playbook.yml"

  end

end