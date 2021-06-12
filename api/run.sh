#!/bin/bash

gunicorn weatherapi.wsgi -w 3 -b 0.0.0.0:8000
