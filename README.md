# simpleF1simulator
A command line/text output simple F1 simulator which gets input data such as driver and car parameters and outputs race results. I started this project as a homework from Introduction to Object-Oriented Programming Languages and Systems class, in Java. Later on, I decided to improve this to a bigger project and converted it into a Python project. Due to limited time I have, it is still a work on progress. One day, I may turn it into a simple video/GUI based simulator.

## How it works
- Simulator takes data from txt/csv files from io folder
- It outputs race results io/out.txt, based on driver, car, tyre, engine data.
- It also outputs pitstops and fastest laps of drivers to the standard output.

## Features
- Some chassis are better than others, each chassis has different downforce multiplier which affects cars' turning performances.
- Engine suppliers, which usually provides an engine more than one team, each have different power multiplier which affects cars' straight line speed.
- 3 different turn types (High speed, medium speed, low speed) all of which has different amount of wear on different type of tyres.
- 3 different compound of tyres, as in current Formula 1 regulations, which affects mechanical grip and tyre wear levels.
- Any amount of different tracks (currently only one) which has similar characteristics to current F1 circuits.
- Pitstops in order to change worn tyres into brand new ones.

## Planned changes
- Change current linear tyre wear model to a better and more natural one
- Add different driver characteristics (aggressive, conservative, being prone to error and so on) which helps variation between different drivers.
