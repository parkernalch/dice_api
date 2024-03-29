# Dice API
A full-stack flask application with API backend
check it out [here](http://apidice.herokuapp.com)

## Dice Notation
    - XdY: roll X many Y-sided dice and return the sum
    
    - XdY!: roll X many Y-sided acing/exploding* dice and return the sum
    
    - [A, B, C]hZ: evaluate the blocks A, B, and C, and then keep the (h)ighest Z values and return their sum
    
    - [A, B, C]lZ: evaluate the blocks A, B, and C, and then keep the (l)owest Z values and return their sum

    *a die that can "explode" or "ace" will keep rolling as long as it rolls the maximum value. (e.g. rolling 1d6! can yield a result greater than six if the rolls are as follows: [6, 6, 3] = 15)

### Future Additions:
- Display array of dice rolled instead of just the roll result
- Create interactive equation builder
- Implement PWA functionality with roll scripts in cache