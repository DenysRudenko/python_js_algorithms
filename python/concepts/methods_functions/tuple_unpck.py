stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for item in stock_prices:
    print(item)

for ticker, price in stock_prices:
    print(price+(0.1 * price))

work_hours = [('Abby', 100), ('Denys', 155), ('Vladyslava', 178)]

def employee_check(work_hours):

    current_max = 0
    employee_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_month = employee
        else:
            pass
    
    return (employee_month, current_max)

print(employee_check(work_hours))

products_per_day = [('banana', 12, 0.70), ('lemon', 2, 0.30), ('strawberry', 17, 2.73)]

def product_check(products_per_day):
    '''
    Function that counts the most selling product per day, and total sum per product
    '''

    product_name = ''
    quantity = 0
    total_price = 0

    for product, total_products, price in products_per_day:

        if total_products > quantity:
            quantity = total_products
            product_name = product
            total_price = price * quantity
        else:
            pass

    return (product_name, quantity, total_price)

print(product_check(products_per_day))


