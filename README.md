# DECALANG

Decalang (dl) is an interpreted shell language used to do simple tasks since this language is only usable on command line/terminal at the time. 


|                                  :warning: WARNING                                  |
|:------------------------------------------------------------------------------------|
| **decalang is not ready to use for big projects and it doesnt include libraries**   |


# WHY DECALANG?

Dl is a fast language and easy to use since it only has 15 keywords

Here is a simple code in three different languages

**Decalang**

```c
fun add(x,y) { 
  send(x + y); 
}
var x = 23;
var y = 12;

add(x,y);
```

**C**

```c
#include <stdio.h>
#include <stdlib.h>

void add(x,y) { printf(x + y); }

int main(int argc, const char argv[]) {
  var x = 23;
  var y = 12;
  add(x,y);
  return 0;
}
```

**Python**

```python
def add(x,y): 
  print(x + y)
x = 23;
y = 12;

add(x + y)
```

# Download (Windows)


Make sure to do every steps right

1- Download the decalang.exe file on the github

2- Create a file with an extension usually .dl or .deca

3- Write your code using the decalang/doc syntax

4- Open as default the type of file you created with decalang.exe

5- execute your program in the terminal with the command [file name].dl or [file name].deca