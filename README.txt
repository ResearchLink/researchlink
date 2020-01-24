# How to run docker

rename the tag if needed(test is the tag for example)

```
sudo docker build -t rl:test .
sudo docker run -d -p 5000:5000 -v /home/ubuntu/Work/uploads:/home/Work/uploads rl:test
```

# notes:
file should be LF