# DECALANG

Decalang (dl) is an interpreted programming language made in rust used to do simple tasks since this language is in heavy developement and currently in beta 


|                                  :warning: WARNING                                  |
|:------------------------------------------------------------------------------------|
| **decalang is not ready to use for big projects because of the limitation of the language**   |


# WHY DECALANG?

Dl is a fast language, easy to use and beginner friendly since it only has 15 keywords to memorize.

Here is a simple code in three different languages including decalang.

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
x = 23
y = 12

add(x,y)
```

# Download Windows OS

**Make sure to do every steps right**


1- Download the `Latest Source Code (zip)` file on the github

2- Unzip the zip file

if you want to use the shell else skip to #4: 3- Execute the `decalang.exe` file located at `/target/release/decalang.exe` to open the shell

4- Create a file with an extension usually `.dl` or `.deca` anywhere you want

3- Write your code using the `/decalang/doc/` syntax

4- Open as default the type of file you created with `decalang.exe`

5- execute your program in the terminal with the command `[file name].dl` or `[file name].deca`

