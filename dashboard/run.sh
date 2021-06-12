#!/bin/bash

gunicorn weatherdash.wsgi:application -w 3 -b 0.0.0.0:8000
