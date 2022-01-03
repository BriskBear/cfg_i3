#!/bin/bash

list=($(cat clone_list))
short=()

for i in ${list[@]}
do
  short+=($(echo $i|rev|cut -f1 -d '/'|rev))
done

clone_loop() {
  for i in $@
  do
    echo $i
    git clone $i /tmp/src/$(echo $i|rev|cut -f1 -d '/'|rev)
  done
}

make_loop() {
  for i in $@
  do
    echo /tmp/src/$i
    pushd /tmp/src/$i && \
    makepkg --noconfirm -sirc
  done
  rm -rvf /tmp/src
}

clone_loop ${list[@]}
make_loop ${short[@]}
