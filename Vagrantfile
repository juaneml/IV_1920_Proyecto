Vagrant.configure('2') do |config|

  #primera configuración vagrant
  config.vm.define :bento_19 do |bento_19|
      config.vm.box = "bento/ubuntu-19.10"
      bento_19.vm.provider :virtualbox do |virtualbox, override|
          # Evitar que busque actualizaciones
          config.vm.box_check_update = false
          # configuramos la red de nuestra máquina
          config.vm.network "forwarded_port", guest: 8000, host: 8000
      end
  end

  #configuración para azure

  config.vm.define :cloud_azure do |cloud_azure|
  config.vm.box = "azure"

  # use local ssh key to connect to remote vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  cloud_azure.vm.provider :azure do |azure, override|

    # each of the below values will default to use the env vars named as below if not specified explicitly
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    azure.vm_name = 'sinhumo1920'
    azure.vm_size = 'Standard_DS2_v2'
    azure.location = 'westeurope'
    azure.tcp_endpoints = "80"
    azure.resource_group_name = 'sinhumo1920'
    azure.vm_image_urn = 'canonical:ubuntuserver:16.04.0-LTS:latest'

    # Evitar que busque actualizaciones
    config.vm.box_check_update = false

    # dns_name
    azure.dns_name = 'sinhumo1920'

  
    end
  end

  #configuración para google cloud
  config.vm.define :sinhumo1920 do |sinhumo1920|
      sinhumo1920.vm.box = "google/gce"
      sinhumo1920.vm.network "forwarded_port", guest: 22, host: 2222
      sinhumo1920.vm.network "forwarded_port", guest: 80, host: 80
      sinhumo1920.vm.network "forwarded_port", guest: 8000, host: 8000
      sinhumo1920.vm.synced_folder ".", "/vagrant", disabled: true, type: "rsync"
      
      sinhumo1920.vm.provider :google do |google, override|
          google.google_project_id = ENV['GOOGLE_PROJECT_ID']
          google.google_json_key_location = ENV['GOOGLE_KEY_LOCATION']
          google.name = "sinhumo1920"
          google.image = "ubuntu-1604-xenial-v20170125"
          override.ssh.username = ENV['GOOGLE_SSH_USER']
          override.ssh.private_key_path = ENV['GOOGLE_SSH_KEY_LOCATION']
      end
  end

  # Configuración  para provisionar con ansible
    config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.version = "2.8.3"
    ansible.playbook = "provision/playbook.yml"

  end
end