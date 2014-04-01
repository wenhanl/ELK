ELK
===

Elasticsearch, Logstash, Kibana stack for log analysis


Current:
-------

- logstash receive data from TCP input interface;
- file input interface problematic;

Usage:
------
- logstash config file: ./logstash/s.conf
- cd logstash
- ./bin/logstash -f s.conf
- open another terminal
- python tcp.py

Problem
-------
- Default pattern matching of access log have parsing problem - solved now
