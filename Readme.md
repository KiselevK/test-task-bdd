# Test task with selenium-behave

This repo provides simple test behave and selenium python pakeges.

### Repo structure:

```
test-task-bdd/
│
├── features/
│   ├── simpletest.feature   # File that describe scenario
│   │
│   └── steps/
│       └── test_steps.py              # Python script with steps for scenario
│
├──behave.ini                       #Conf file for behave
│
├── Dockerfile                          # Dockerfile to build the image
│
└── requirements.txt                    # list of Python requirements
```

### How to use

Simple way

```
docker pull kilimanjaroo/test-task-selenium-behave:latest
docker run -v ./output:/app/output kilimanjaroo/test-task-selenium-behave:latest
```

with git docker

```
git pull https://github.com/KiselevK/test-task-bdd.git
cd test-task-bdd
docker build -t ftest . 
docker run -v ./output:/app/output ftest
```

just run test

```
git pull https://github.com/KiselevK/test-task-bdd.git
cd test-task-bdd
behave
```

### Example

* There is an example of execution https://dev.azure.com/kirillkiselev220/perf%20staff/_build/results?buildId=96&view=results
* And there is an output result https://dev.azure.com/kirillkiselev220/perf%20staff/_build/results?buildId=96&view=artifacts&pathAsName=false&type=publishedArtifacts
