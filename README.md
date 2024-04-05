# csci3010u-project
This is a simulation of the Plinko board game

## Running
This project uses pygame for rendering and scipy/numpy for numerical
calculation. As long as a recent version of these libraries are on your system it
should work just fine. I used pipenv for dependency management so that will work
as well.

native python (make sure that the dependency's are installed)
```sh
python3 main.py
```
with pipenv
```sh
pipenv run python3 main.py
```
## Playing
When the game has loaded up the Plinko board should show up. it will be filled
with pegs, and to add balls you simply have to click the mouse where you would
like to spawn the ball. you can add as many balls as you like to whatever part
of the board you wish. To quit just press the x on the game window.
