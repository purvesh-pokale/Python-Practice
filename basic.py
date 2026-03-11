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