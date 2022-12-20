# AirBnB Clone
![AirBnB](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

AirBnB Clone is simple copy of the AirBnB website. The goal of this project is to build a simple copy of the AriBnB website on my own server.

Here, the goal is to build a **command-line interface** to maniplate data without a visual interface, like in a *Shell* (perfect for development and debugging). This will be the first part of constructing the full web application. Further, I will have a front-end that shows the final product to everybody: static and dynamic, a database or files that store data (data = objects), and an API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The Console
A *command-line interface* to manipulate data without having a visual interface, like in a *Shell* (perfect for development and debugging).
- Create a data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to file(JSON file)

This is the first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored. This abstraction will allow me to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

# How to use the Console?

