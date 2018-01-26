#!/usr/bin/env bash

kubectl delete -f deployment/fodeo-camera
kubectl delete -f deployment/fodeo-fog
kubectl delete -f deployment/fodeo-central
