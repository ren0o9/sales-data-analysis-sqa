Initialize maxSales = 0
Initialize bestProduct = null
Initialize productCount = 0

For each product in products:
    productCount = productCount + 1
    If totalSales > maxSales:
        maxSales = totalSales
        bestProduct = product

Output bestProduct
Output productCount
