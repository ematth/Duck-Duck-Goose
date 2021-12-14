# Duck-Duck-Goose

This is a course project for MUS 305 at the University of Illinois Champaign-Urbana, under the course direction of Dr. Heinrich Taube

- This program uses the musx library to create random compositions based on the children's game "Duck Duck Goose"
- Each composition uses a variety of instruments, of which includes piano, woodwinds like flute and clarinet, brass like trumpets and trombones, and percussion like    xylophone, woodblock and a blown bottle.

# Running the program
- In a terminal, locate the project file's directory and type `python -m duckduckgoose'
- A number of arguments can be called, in the following order:
  - `seed` defines a specific seed integer from which to generate randomization in the composition.
  - `phrase length` defines an integer from which to decide how many measures each phrase (the "duck" phrase, the "goose" phrase) go on for.
  - `pitch` defines the starting pitch and the key of the composition. This is a number from 0-11 where 0=C major and 11=B major.
  - `repeats` defines the number of repeats of the "Duck Duck Goose" game to play before ending the composition.
- Each argument listed can be either defaulted or specified, but they must all be in order. You can define any argument as -1 to automatically default its value.
  - For example: `python -m duckduckgoose -1 -1 5 -1` is a default composition in the key of F major (pitch=5).
  - Another example: `python -m duckduckgoose 37 -1 -1 4` is a composition with a set seed that is repeated 4 times.
