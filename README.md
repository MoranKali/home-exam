# home-exam

Hey!

I would like to explain my thought process when I received the assignment.
Well, I had to start with CloudFormation and setup my infra, so I started reading about it to figure out the best way. I found out there's a built-in tool to convert existing infra to YAML. 
Fantastic, right? Wrong. 
In the infra/auto-generated folder, you'll find the absolute abominations this tool produced.
I did get everything else though. And I would've had time to add monitoring too, if not for CF.

The two json files in infra are used by the CI/CD, which I used GitHub Actions for.
The two ecr-from-scratch YMLs and the ecs-cluster.yml are actually supposed to work in CF.
The rest are... we'll see. 

1) create registry for ms1 & ms2.
2) create ALB.
3) create ecs cluster.
4) create task def for ms1.
5) create service for ms1, connect to alb.
6) create queue.
7) create S3 bucket.
8) create task def for ms2.
9) create service for ms2.

