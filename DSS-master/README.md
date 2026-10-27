# Distributed Software Systems # 
## Course project for "Verteilte Software-Anwendungen" ##


A Distributed Software System (DSS) describes a collection of independent software components that run in separate processes or on different computers and communicate over a network to accomplish a common task.

Unlike a centralized application, a distributed system must account for network communication, synchronization, concurrency, and partial failures.

### Overview ###
This repository accompanies the development of a practical course on DSS at Hochschule Bielefeld (HSBI). It explores how independent software components communicate, process data, handle failures, and work together as one application.

The course uses an industrial data-processing scenario: simulated machines generate time-dependent sensor signals, which are exchanged between services, processed, stored, analyzed for anomalies, and eventually visualized. The system is developed incrementally, moving from simple simulations to a distributed microservice architecture.
**Podman is used instead of Docker** to meet the project's container tooling and licensing requirements.

### Course Objectives ### 
The goal of the course is to understand the fundamental principles of distributed software systems through the step-by-step development of a container-based application.

Students will learn to design and connect microservices using REST APIs, manage containers with Podman, process and store machine-generated data, and implement basic anomaly detection, testing, and monitoring.

The practical project begins with two simulated machines generating sine and cosine signals and gradually develops into a distributed application.

The remaining README sections, including the architecture, 14-session lecture outline, and development roadmap, are preserved.



### Project scenario ### 

### Course outline ###

