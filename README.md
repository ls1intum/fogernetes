
_A platform for the deployment and management of fog computing applicatoins using a label-based requirements & capabilities mapping process._

This version of Fogernetes is based upon the work described in

> [Cecil Wöbker](https://cwoebker.com/research), [Andreas Seitz](https://www1.in.tum.de/lehrstuhl_1/index.php/people/616-andreas-seitz), Harald Mueller, and [Bernd Bruegge](https://www1.in.tum.de/lehrstuhl_1/people/52-professorm) <br>
> **[Fogernetes: Deployment and Management of Fog Computing Applications]()** <br>
> Submitted for the [IEEE/IFIP International Workshop on Decentralized Orchestration and Management of Distributed Heterogeneous Things (DOMINOS’2018)](https://sites.google.com/view/dominos2018/), <br>
> Marc-Oliver Pahl, Hanan Lutfiyya, Jeremy Singer, Steven Johnston, and Colin Perkins, April 2018, Taipei, Taiwan.

If you wish to reuse parts of this repo, please cite the above mentioned article.

## Intro

Devices used in fog and edge computing are heterogeneous, decentralized and distributed. 
These computing environments are unpredictable and their applications are becoming more complex. 
This leads to challenges regarding deployment and management of fog and edge applications.   
It is important to ensure that quality of service, availability, reliability and real-time characteristics are guaranteed during deployment to take advantage of fog computing.
In this paper, we present **Fogernetes**, a fog computing platform that enables management and deployment of fog applications with specific requirements on heterogeneous devices with different capabilities.
Fogernetes allows matching requirements of application components with device capabilities by using a labeling system.
Based on a case study, we evaluate and test Fogernetes and examine its practical applicability for the deployment and management of fog computing applications.
Fodeo serves as an example application. 
Fodeo analyzes video streams from multiple cameras and detects objects in them. 
Fogernetes enables the deployment of Fodeo components on appropriate devices by matching requirements and capabilities.

### Fodeo

`fodeo/`

We present Fodeo (**Fo**gVi**deo**), a custom fog application we created for testing and evaluating Fogernetes.

Fodeo is a surveillance application that delivers and analyzes videos from multiple cameras.
The video signal is recorded and analyzed in a cloud component. 
Fodeo applies fog computing to improve the video delivery performance.
Fodeo manages to save bandwidth by filtering incoming data and sending compressed video data to the cloud.
The following figure shows the 4 Fodeo components and their relation.

<img src="https://github.com/ls1intum/fogernetes/blob/master/img/FodeoDesign.png" width="400">

## Deployment

`fodeo/deployment`

Using the power and versatility of Kubernetes we can deploy the Fodeo components with just a few lines of code.

```
#!/usr/bin/env bash

kubectl create -f deployment/fodeo-central
kubectl create -f deployment/fodeo-fog
kubectl create -f deployment/fodeo-camera
```

The resulting deployment can be seen below.

<img src="https://github.com/ls1intum/fogernetes/blob/master/img/FodeoMapping.png" width="500">


## Quick Setup Guide

`setup/`

You can find some basic setup scripts in the "setup" directory.

* **prepare.sh**
* **create.sh**
* **join.sh**
