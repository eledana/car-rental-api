from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json

uri = "neo4j://localhost:7687" 
auth = ("neo4j", "password")

def get_connection() -> Driver:
    driver = GraphDatabase.driver(uri, auth=auth)
    driver.verify_connectivity()
    print("Connection successful.")
    return driver

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

# Used curriculum and presentations for solving task

# Car methods

class Car:
    def __init__(self, make, model, year, location, reg):
        self.make = make
        self.model = model
        self.year = year
        self.location = location
        self.reg = reg

def create_car(make, model, year, location, reg):
    cars = get_connection().execute_query("MERGE (a:Car{make:$make, model:$model, year:$year, location:$location, reg:$reg}) RETURN a;",
    make = make, model = model, year = year, location = location, reg = reg)
    nodes_json = [node_to_json(record["a"] for record in cars)]
    print(nodes_json)
    return nodes_json

def read_cars():
    with get_connection().session() as session:
        cars = session.run("MATCH (a:Car) RETURN a;")
        nodes_json = [node_to_json(record["a"] for record in cars)]
        print(nodes_json)
        return nodes_json
    
def findCarByReg(reg):
    with get_connection().session() as session:
        cars = session.run("MATCH (a:Car) where a.reg=$reg RETURN a;", reg=reg)
        print(cars)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json

def update_car(make, model, year, location, reg):
    with get_connection().session() as session:
        cars = session.run("MATCH (a:Car{reg:$reg}) set a.make=$make, a.model=$model, a.year=$year, a.location=$location RETURN a;", make=make, model=model, year=year, location=location, reg=reg)
        print(cars)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json
    
def delete_car(reg):
    get_connection().execute_query("MATCH (a:Car{reg:$reg}) delete a;", reg=reg)

# Customer methods

class Customer:
    def __init__(self, id, name, age, address):
        self.id = id
        self.name = name
        self.age = age
        self.address = address

def create_customer(name, age, address):
    customers = get_connection().execute_query("MERGE (a:Customer{id:$is, name:$name, age:$age, address:$address}) RETURN a;",
    id=id, name=name, age=age, address=address)
    nodes_json = [node_to_json(record["a"] for record in customers)]
    print(nodes_json)
    return nodes_json

def read_customers():
    with get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) RETURN a;")
        nodes_json = [node_to_json(record["a"] for record in customers)]
        print(nodes_json)
        return nodes_json
    
def findCustomer(id):
    with get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) where a.id=$id RETURN a;", id=id)
        print(customers)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        print(nodes_json)
        return nodes_json

def update_customer(id, name, age, address):
    with get_connection().session() as session:
        customers = session.run("MATCH (a:Customer{id:$id}) set a.name=$name, a.age=$age, a.address=$address RETURN a;", id=id, name=name, age=age, address=address)
        print(customers)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        print(nodes_json)
        return nodes_json
    
def delete_customer(id):
    get_connection().execute_query("MATCH (a:Customer{id:$id}) delete a;", id=id)

# Employee methods

class Employee:
    def __init__(self, id, name, address, branch):
        self.id = id
        self.name = name
        self.address = address
        self.branch = branch

def create_employee(id, name, address, branch):
    employees = get_connection().execute_query("MERGE (a:Employee{id:$is, name:$name, address:$address, branch:$branch}) RETURN a;",
    id = id, name = name, address = address, branch = branch)
    nodes_json = [node_to_json(record["a"] for record in employees)]
    print(nodes_json)
    return nodes_json

def read_employees():
    with get_connection().session() as session:
        employees = session.run("MATCH (a:Employee) RETURN a;")
        nodes_json = [node_to_json(record["a"] for record in employees)]
        print(nodes_json)
        return nodes_json
    
def findEmployee(id):
    with get_connection().session() as session:
        employees = session.run("MATCH (a:Employee) where a.id=$id RETURN a;", id=id)
        print(employees)
        nodes_json = [node_to_json(record["a"]) for record in employees]
        print(nodes_json)
        return nodes_json
    
def update_employee(id, name, address, branch):
    with get_connection().session() as session:
        cars = session.run("MATCH (a:Employee{id:$id}) set a.name=$name, a.address=$address, a.branch=$branch RETURN a;", id=id, name=name, address=address, branch=branch)
        print(cars)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json
    
def delete_employee(id):
    get_connection().execute_query("MATCH (a:Employee{id:$id}) delete a;", id=id)


        