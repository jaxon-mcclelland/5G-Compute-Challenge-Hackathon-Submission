# 5G-Edge-Hackathon-Submission

## Inspiration
 We were inspired to make this project due to the nature of 5G, with 5G encouraging decentralized applications that allow us to access large amounts of data with low latency across a large area. We felt the perfect way to show this was through a weather related app.
## What it does
Our application collects pressure, temperature, magnetometer, and humidity from Raspberry Pi 4 IoT devices using Verizon's 5G network and then aggregates it into an API for users to pull from, as well as a proof of concept dashboard to visualize available data in a 24 hour period.
## How we built it
We built our setup using a virtual private cloud in AWS, with an AWS Wavelength zone to allow our Django API server to collect data from our IoT devices over 5G. We then stored that data into a low latency MySQL RDS database, allowing it to be accessed by our client side API and our PoC Dashboard. All instances were run using docker containers within an EC2 instance.
## Challenges we ran into
The main issues we ran into were relating to the Amazon AWS Services that connected our IoT devices via the wavelength network. Going into this project, our team was not very well versed in the inner workings of AWS services outside the standard Route 53 and EC2 services. When using AWS VPC we had difficulties finding a secure way to configure our services without causing issues for ourselves, which eventually resulted in our use of an SSH bastion to configure our EC2 instances. We also had problems with Wavelength connectivity, which required us to research proper use of carrier gateways for our VPC. 
## Accomplishments that we're proud of
Our infrastructure is efficient and easily scalable due to our decentralized mesh plug and play networks. In addition, we are proud of the time and energy we put into researching and building out our functional AWS virtual private cloud connecting our IoT devices via the wavelength network to our ECS and RDS services. Outside of our final product, we are proud of the time management and organization skills we put to use to ensure our project ran smoothly and on time, ending with an ontime final submission.
## What we learned
We improved our abilities to devise and implement infrastructure in AWS, learned how to implement applications in AWS Wavelength, and improved our teamwork and communication skills.
## What's next for 5G Weather IoT Devices
* Additional Devices
* Mass Purchasing of Devices for Price Reduction
* Using 5G Hotspots for Lower Latency
* Splunk Logging of IoT Device Logs
* Active Device Tracking for Security and Asset Management
