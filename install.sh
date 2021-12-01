#!/bin/bash

#Script for create venv and install needed package mrUtility


create_venv(){
    echo create venv
    python3 -m venv /opt/lispio/mrUtility/mrUtility_venv
    echo done
}

install_py_package()
{
  echo insall requirements package
  source /opt/lispio/mrUtility/mrUtility_venv/bin/activate
  pip install wheel
  pip install -r /opt/lispio/mrUtility/requirements.txt
  deactivate
  echo done
}

create_venv
install_py_package
