#!/bin/bash

ifconfig | awk '$1 == "inet"{print$2}'
