from connect import connect_sql

def retrieve_products(connection):
    cursor = connection.cursor()
    my_query = ("SELECT products.product_id, products.product_name, products.unit_id, products.unitprice, unit.unitname "
                "FROM products inner join unit on products.unit_id = unit.unit_id")
    cursor.execute(my_query)
    response = []
    for (product_id, product_name, unit_id, unitprice, unitname) in cursor:
        response.append({
            'product_id': product_id,
            'name': product_name,
            'unit_id': unit_id,
            'unitprice': unitprice,
            'unitname': unitname
        })
    return response

def insert_new(connection, products):
    cursor = connection.cursor()
    my_query = ("INSERT INTO products"
                "(product_name, unit_id, unitprice)"
                "VALUES (%s, %s, %s)")
    new = (products['product_name'], products['unit_id'], products['unitprice'])

    cursor.execute(my_query, new)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    my_query = ("DELETE FROM products WHERE product_id=" + str(product_id))
    cursor.execute(my_query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = connect_sql()
    print(retrieve_products(connection))
    print(insert_new(connection, {
        'product_name': 'potatoes',
        'unit_id': '1',
        'unitprice': 100
    }))
    

