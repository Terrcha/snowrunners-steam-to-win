import os
from main import (
    load_container,
    load_saves
)

def test_container_load():
    save_loc =f"{os.getcwd()}/output"
    assert "container" in load_container(save_loc)

def test_file_load():
    container = f"{os.getcwd()}/output/container.115"
    assert load_saves(container)

    