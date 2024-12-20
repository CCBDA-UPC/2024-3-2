**Task 3.1**

In the first task, we were shown how to work with Identity and Access Management(IAM) dashboard.
The most important and useful tabs of that dashboard are User groups, Users, and Policies.
The laboratory taught us how to navigate between different users and user groups(adding or removing users from a user group),
how to inspect and read given policies to a group of users or to a specific user.

![Task3.1.png](images/Task3.1.png)

**Task 3.2**

In the second task, the main focus was on VPCs. We started off by creating our own VPC.
There are plenty of different settings that we can change according to our needs, for instance,
number of availability zones, number of public or private subnets, VPC endpoints, etc. This is what you see
after creating a VPC

![Task3.2.1.png](images/Task3.2.1.png)

We then proceeded to the creation of additional subnets and editing subnet associations through
route tables.

![Task3.2.2.png](images/Task3.2.2.png)

To allow web requests we altered VPC's security group a little bit by creating a specific rule.
Lastly, we launched our web server on a EC2 instance. As in VPC creation, when launching EC2 instance
we are offered many different setting that we can change according to our needs, for instance, Quick Start AMIs (we can also create our own AMI),
instance type, network and its subnet, storage, etc.

**Task 3.3**

The third task was somewhat similar to the second task to some extent. We started from launching EC2 instance
and configuring its settings. The difference from the previous task is that this EC2 instance
has termination protection enabled.

![Task3.3.png](images/Task3.3.png)

We then learnt how to get system log and instance screenshot. Then instead of creating a new
security group attached to the instance we updated the one instance uses. We also changed
the instance type (the instance was stopped earlier), changed stop protection, and resized EBS volume.


**Task 3.4/3.5**

For the task 3.5 we had to use AWS rekognition instead of AWS comprehend. AWS rekognition has plenty of different methods for analysis, comparison, and describing of images. However, most of the methods it has are related to humans and specifically to facial images. That is why we decided to use methods related to people as there are more of those available.The most time demanding task was going through each available method and reading its required inputs and what are its outputs. After that we decided to build a small program utilizing 2 methodscompare_faces and detect_faces. Firstly, the program compares the given face image to all other face images available. 
Compare_faces also requires similarity_threshold value which decides how strict comparison must be. 
By default, it is set to 80 but it can be changed by user if he wants the comparison to be less strict. 
For each image that has been matched, meaning its similiraty_threshold is higher, we provide 4 outputs which are age_range, gender, smile, and eyeglasses. 

We also tried detect_labels method in the much simpler version of code called Comprehend1.py. The method has many different outputs that could be used in a variety of tasks but it seemed unnecessary in our case.