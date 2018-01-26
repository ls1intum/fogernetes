#!/usr/bin/env bash

kubectl create -f deployment/fodeo-central
kubectl create -f deployment/fodeo-fog
kubectl create -f deployment/fodeo-camera
