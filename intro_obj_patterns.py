## 3 types of Design patterns
# 

# creational
##  used to create objects in a systematic way
##  benefits include flexibility

# structural
##  establish useful relationships between software components
##  functional and nonfunctional goals

# behavioral 
##  best practices of object interaction
##  define protocols

# object oriented mechanisms used
##  creational = polymorphism
##  structural = inheritance
##  behavioral = methods and their signatures


# object orientation
## patterns are primarily geared towards objects and classes

# classes - templates to create objects - cookie clutter objects replications
# Attributes - captures the state of an object, represents the properties of an object
# Methods - represents behaviors of an object
# for example
##  Partcipant.age
##  Participant.cancel()


# Inheritance
##  establishes parent and child relationship of Classes and its instances
##  Pet class --> Dog class and Cat class

# Polymorphism
##  child classes can be instantiated and transformed into parent class
##  Pet class --> true nature of object is at runtime, so we don't know right now if it's cat or dog

# Pattern contexts
##  what patterns work best in what contexts 
##  contexts contain:
    ## participants
        ## involved in forming the design pattern, to accompish the goal of the pattern
    ## quality attributes
        ## nonfunctional requirements 
        ## effects the entire software
        ## addressed by architecture
    ## forces
        ## various factors or trade offs
        ## often manifested in quality attributes, so good to list and reason out quality attributes well
    ## consequences
        ## decision makers
        ## choosing despite the trade offs
        ## for example, better security but worse off performance


# Pattern Language
##  name, context, problem, solution, and related patterns
## focus on meaning, design challenge to address, and specify the pattern itself in structure, relationships, interactions, and behaviors
## note similar but different as well as linked together patterns 


class Pet():
    pass

class Dog(Pet):
    pass

class Cat(Pet):
    pass

print(Pet, Dog, Cat)
