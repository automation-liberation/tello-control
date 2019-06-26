def label = "worker-${UUID.randomUUID().toString()}"
def properties

podTemplate(label: label, containers: [
    containerTemplate(name: 'python', image: 'python:3.7', command: 'cat', ttyEnabled: true),
    containerTemplate(name: 'helm', image: 'lachlanevenson/k8s-helm:v2.14.0', command: 'cat', ttyEnabled: true),
    containerTemplate(name: 'deployment-helper', image: 'irori.johansson.tech/automation-liberation/deployment-helper:latest', command: 'cat', ttyEnabled: true),
    containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true)
    ],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
], imagePullSecrets: [ 'docker-registry-credentials' ]) {
    node(label) {
        stage('Build') {
            git 'https://github.com/automation-liberation/tello-control.git'
            script {
                properties = readYaml file: "build-properties.yaml"
            }
        }

        stage('Push Docker Image') {
            container('docker') {
                withCredentials([[$class: 'UsernamePasswordMultiBinding',
                    credentialsId: 'irori',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASSWORD']]) {
                    sh """
                        docker login -u ${USER} -p ${PASSWORD} https://${properties.image.registry}
                        docker build -t ${properties.image.registry}/${properties.image.package}:${properties.image.tag} .
                        docker push ${properties.image.registry}/${properties.image.package}:${properties.image.tag}
                    """
                }
                sh "docker rmi ${properties.image.registry}/${properties.image.package}:${properties.image.tag}"
            }
        }

        stage('Deploy') {
            container('helm') {
                dir('charts') {
                    sh "helm upgrade tello-control tello-control --install --set image.tag=${properties.image.tag}"
                }
            }
        }
        stage('Update Changelog') {
            container('deployment-helper') {
                sh 'deployment-helper changelog -p build-properties.yaml'
            }
        }
    }
}
