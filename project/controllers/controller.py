from project import app
from flask import render_template, request, redirect, url_for
from project.models.model import *

# Cars

@app.route("/create_car", methods=["POST"])
def create_new_car():
    record = json.loads(request.data)
    print(record)
    return create_car(record["make"], record["model"], record["year"], record["location"], record["reg"])

@app.route("/get_cars", methods=["GET"])
def query_records():
    return read_cars()

@app.route("/get_cars_by_reg_number", methods=["POST"])
def find_car_by_reg_number():
    record = json.loads(request.data)
    print(record)
    print(record["reg"])
    return findCarByReg(record["reg"])

@app.route("/update_car", methods=["PUT"])
def update_car_info():
    record = json.loads(request.data)
    print(record)
    return update_car(record["make"], record["model"], record["year"], record["location"], record["reg"])

@app.route("/delete_car", methods=["DELETE"])
def delete_car_info():
    record = json.loads(request.data)
    print(record)
    delete_car(record["reg"])
    return read_cars()

# Customers

@app.route("/create_customer", methods=["POST"])
def create_new_customer():
    record = json.loads(request.data)
    print(record)
    return create_customer(record["id"], record["name"], record["age"], record["address"])

@app.route("/get_customers", methods=["GET"])
def query_customers():
    return read_customers()

@app.route("/find_customers_by_id", methods=["POST"])
def find_customers_by_id():
    record = json.loads(request.data)
    print(record)
    print(record["id"])
    return findCustomer(record["id"])

@app.route("/update_customer", methods=["PUT"])
def update_customer_info():
    record = json.loads(request.data)
    print(record)
    return update_customer(record["id"], record["name"], record["age"], record["address"])

@app.route("/delete_customer", methods=["DELETE"])
def delete_customer_info():
    record = json.loads(request.data)
    print(record)
    delete_customer(record["id"])
    return delete_customer()

# Employees

@app.route("/create_employee", methods=["POST"])
def create_new_employee():
    record = json.loads(request.data)
    print(record)
    return create_employee(record["id"], record["name"], record["address"], record["branch"])

@app.route("/get_employees", methods=["GET"])
def query_employees():
    return read_employees()

@app.route("/find_employees_by_id", methods=["POST"])
def find_employees_by_id():
    record = json.loads(request.data)
    print(record)
    print(record["id"])
    return findEmployee(record["id"])

@app.route("/update_employee", methods=["PUT"])
def update_employee_info():
    record = json.loads(request.data)
    print(record)
    return update_employee(record["id"], record["name"], record["address"], record["branch"])

@app.route("/delete_employee", methods=["DELETE"])
def delete_employee_info():
    record = json.loads(request.data)
    print(record)
    delete_employee(record["id"])
    return delete_employee()
