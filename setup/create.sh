#!/bin/env bash

sudo kubeadm init --apiserver-advertise-address=131.159.38.35
sudo cp /etc/kubernetes/admin.conf $HOME/
sudo chown $(id -u):$(id -g) $HOME/admin.conf
export KUBECONFIG=$HOME/admin.conf
kubectl apply -f https://git.io/weave-kube-1.6
kubectl create -f https://rawgit.com/kubernetes/dashboard/master/src/deploy/kubernetes-dashboard.yaml
kubectl apply --filename https://raw.githubusercontent.com/giantswarm/kubernetes-heapster/master/manifests-all.yaml

## untaint master

kubectl --kubeconfig ../secret/admin.conf taint nodes vmbruegge45 node-role.kubernetes.io/master:NoSchedule-
