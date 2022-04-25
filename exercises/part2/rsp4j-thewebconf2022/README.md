# RSP4J @ the Web Conf 2022 ![Alt text](https://raw.githubusercontent.com/streamreasoning/rsp4j/master/figs/rsp4jLogo.svg)

This repository contains the examples and exercises for the RSP4J tutorial at the Web Conf 2022.

We will use a covid scenario consisting of two room (BlueRoom and RedRoom) and 4 types of streams:
1. RFID observations that report the location of a person through RFID tags.
1. Facebook check-in posts that also report the location of a person.
1. Contact tracing posts that report the presence of two individuals.
1. Testing results posts that report the results of a corona test a certain individual took.

The figure below shows the setup of the corona scenario.
![Corona scenario](fig/covid_scenario.png) 

Each of the streams typically come in a variaty of data formats (e.g. json, csv, xml, etc.). 
For simplicty, we show them here in tabular format and how they are mapped to the semantic model:

![Corona scenario](fig/covid_data.png) 

During the examples and exercises, we will look at solving the following queries:
![Corona scenario](fig/covid_queries.png) 

## Getting started

To get started clone this repository:
```
git clone https://github.com/pbonte/WSP-TheWebConf2022Tutorial
```

Move to the rsp4j-bigdata2021 folder and compile through maven:
```
cd exercises/part2/rsp4j-thewebconf2022/
mvn clean install -DskipTests
```

Open the project with your favorate IDE, e.g. IntelliJ or Eclipse.

You can find the examples in the folder `src/main/java/org/streamreasoning/rsp4j/thewebconf2022/processing/examples/` and the assignments in `src/main/java/org/streamreasoning/rsp4j/thewebconf2022/processing/assignments/`.

# RSP4J

RSP4J is an API for the development of RSP engines. More information can be found on the [RSP4J website](https://github.com/streamreasoning/rsp4j).
We welcome any kind of contribution, please check the [contribution document](https://github.com/streamreasoning/rsp4j/blob/master/CONTRIBUTING.md) for more information.
