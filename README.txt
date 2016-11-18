
///////////////////////////////Setting up Virtual Python Environment
virtualenv code_11_18
source code_11_18/bin/activate

//////////////////////////////////////// Setting up Nupic Dev Environment //////////////////////////////////////////
sudo yum group install "Development Tools"
sudo yum install python-devel.x86_64
wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
sudo yum update
sudo yum install mysql-server
sudo systemctl start mysqld
git clone https://github.com/csbond007/Numenta-Anomaly-Detection.git  // Git repository to be cloned
curl https://bootstrap.pypa.io/get-pip.py | sudo python
pip install nupic
pip install cassandra-driver
pip install pandas

/////////////////////////////////////////// Cassandra Table Creation /////////////////////////////////////
use table_creation.txt within the cassandra_scripts folder to create the corresponding tables

/////////////////////////////// Running the code /////////////////////////////////////
cd Numenta-Anomaly-Detection

./cleanup.py   // Removes all generated files so you can start from scratch.
./swarm.py     // Run Swarm to build model (Uses Particle Swarm Optimization to build model parameters)

check in model_params whether new model file was created

./run.py   // Run the Model to give generate anomaly scores and related other cassandra tables

Training Data : heart-beat.csv  // For now the data is here, we need to create data-pipelines
Testing Data  : anomaly-data.csv  // For now the data is here, we need to create data-pipelines

Easy Approach to Servicify is to call the main methods of swarm.py and run.py, one after another in a something like service.py

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

