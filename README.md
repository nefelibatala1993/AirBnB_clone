# AirBnB Clone
![AirBnB](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221220%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221220T145242Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=49f5ab8c766bc4203bd056c574cbc5c579bfe2a556771ea94fd9f44d97282d62)
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

