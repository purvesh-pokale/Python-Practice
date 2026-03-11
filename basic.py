'''
#1.python is a compile or interpreted langauage?

The short answer is: Python is both, but it is primarily classified as an interpreted language.

It's a common misconception that a language must be one or the other. 
In reality, Python uses a two-step process to turn your code into something the computer can actually run.

How Python Works Under the Hood
When you "run" a Python script, two distinct stages occur:

Compilation (to Bytecode): First, Python automatically compiles your source code (.py) into an intermediate format called Bytecode (.pyc). 
                           This isn't machine code that your CPU understands; it's a lower-level representation optimized for the next step.

Interpretation (The Virtual Machine): The Python Virtual Machine (PVM) then reads that bytecode and executes it line-by-line. 
                                      This is the "interpreted" part of the process.

Why we call it "Interpreted"
Even though there is a compilation step, we call Python an interpreted language because:

The user doesn't see the compilation: Unlike C++ or Rust, where you must manually run a compiler to create an executable file, 
Python handles it automatically in the background.

Line-by-line execution: The PVM executes the bytecode one instruction at a time, 
rather than loading a massive pre-compiled binary into memory all at once.

'''

'''
Dynamic Typing:-
Dynamic typing refers to what a variable is. In Python, you don't have to declare if a variable is a number, a string, or a list. 
The "type" is associated with the value, not the variable name.
'''
'''
Dynamic Binding
Dynamic binding (also known as late binding) refers to which piece of code gets called. 
It's about how Python links a name (like a function or method) to an actual implementation at the very last moment.

How it works: Python doesn't decide which method to run until it reaches that specific line of code. 
It looks at the object, checks its methods, and "binds" the call to the correct function right then and there.

The Benefit: This allows for Polymorphism. You can have different objects (like a Circle and a Square) that both have a .draw() method, 
and Python will figure out which one to use based on the object's identity at runtime.
'''