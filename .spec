#!/bin/bash

list=($(cat clone_list))
short=()

for i in ${list[@]}
do
  short+=($(echo $i|rev|cut -f1 -d '/'|rev))
done

clone_group() {
  printf '%s\n' "$@"|xargs -I % git clone % /tmp/src/$(echo %|awk '{print $NF}')
#   for i in $@
#   do
#     echo $i
#     git clone
#   done
}

make_loop() {
  for i in $@
  do
    echo /tmp/src/$i
    pushd /tmp/src/$i && \
    makepkg -sric --noconfirm && 
  done
  rm -rvf /tmp/src
}

clone_group ${list[@]}
make_loop ${short[@]}
