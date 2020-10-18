pipeline {
    agent any
     
    stages {
      stage('checkout') {
           steps {
             
                git branch: 'master', url: 'https://github.com/Myraa/pythonlogsrepo.git'
             
          }
        }
         stage('Tools Init') {
            steps {
                script {
                    echo "PATH = ${PATH}"
               def tfHome = tool name: 'Ansible'
                env.PATH = "${tfHome}:${env.PATH}"
                 sh 'ansible --version'
                    
            }
            }
        }
        
        stage('Ansible Deploy') {
             
            steps {
               sh "ansible-playbook main.yaml -i inventories/dev/hosts --user ubuntu --key-file ~/.ssh/id_rsa"  
            }
        }
    }
}