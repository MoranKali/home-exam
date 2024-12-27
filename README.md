# home-exam

## Intro
Hey!

I would like to explain my thought process when I received the assignment.
Well, I had to start with CloudFormation and setup my infra, so I started reading about it to figure out the best way. I found out there's a built-in tool to convert existing infra to YAML. 
Fantastic, right? Wrong. 
In the **infra/auto-generated** dir, you'll find the absolute abominations this tool produced.
I did get everything else though. And I would've had time to add monitoring too, if not for CF.
See live demo on **"Well it works on my machine.7z"**.

The two json files in infra are used by the CI/CD, which I used GitHub Actions for.
CF templates that should work
* ecr-from-scratch-ms1.yml
* ecr-from-scratch-ms2.yml
* ecs-cluster.yml
* s3-bucket.yml


## To reproduce my solution

1) create registry for ms1 & ms2.
2) create ALB.
3) create ecs cluster.
4) create task def for ms1.
5) create service for ms1, connect to alb.
6) create queue.
7) create S3 bucket.
8) create task def for ms2.
9) create service for ms2.

## Conclusion 

I honestly enjoyed the assignment. I learned a few new tools, and dusted off some skills. 
Check out Marshmallow, in ms1! 
Saved me a bit of JQ :)
