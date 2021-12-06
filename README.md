# YET ANOTHER PYTHON ROGUELIKE (YAPR)

This project is a python rogue-like game made with **BearLibTerminal**.

## Why
___
Main reason I created this project is that I wanted to learn something new while programming myself. So here you can see a lot of (probably) poor decisions and much refactoring.

## What is inside
___
Inside this project you can find my interpretation of **Entity-Component-System**. I am improving it from time to time when I find weak spots. 

## How it works
___
It uses quite classic ECS (as I see it). You use entities to contain components, use systems to make logic of the game. 

- **System manager** contains all the logic with systems
- **Entity manager** contains all the logic with entities
- **Context** containing all the managers 
- **Scene manager** contains all the scenes used in the game and the logic to play them

**Entities** have tag system that is being used almost in every system to lower the algorithm complexity (it may get quite laggy if you use all the entities all the time in the systems)

## What I want to be in this project
___
- Inventory
- Enemies
- Enemies AI
- Persona like fight system (Not using your hero to fight but instead use spirits to fight for you against another spirits)
- Affix crafting system
- Level editor
- Campaign
- Story (???)

Will be updated in future.

## How to start
___
You should have python3 and BearLibTerminal installed.

You can start game by console command "python main.py" or via starting start.bat in game folder.

## Contributing
___
If you get how the system works and you have ideas and the most important **MOTIVATION**, you can make pull request and I will be happy to check it!


## Dependencies
___
- BearLibTerminal