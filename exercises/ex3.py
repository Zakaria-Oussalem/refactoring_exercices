""" 
This script applies different discounts based on product categories.
It defines a main function that takes a product dictionary and calculates the final price after applying the appropriate discount."""

def main(product):
    if product['category'] == 'electronics':
        discount = product['price'] * 0.10
        final_price = product['price'] - discount
        print(f"Electronics Discount: ${discount:.2f}")
        return final_price
    elif product['category'] == 'clothing':
        discount = product['price'] * 0.15
        final_price = product['price'] - discount
        print(f"Clothing Discount: ${discount:.2f}")
        return final_price
    elif product['category'] == 'books':
        discount = product['price'] * 0.05
        final_price = product['price'] - discount
        print(f"Book Discount: ${discount:.2f}")
        return final_price
    else:
        print("No discount available.")
        return product['price']

# Example usage

if __name__ == "__main__":
    
    product1 = {'name': 'Laptop', 'price': 1000.00, 'category': 'electronics'}
    product2 = {'name': 'T-Shirt', 'price': 20.00, 'category': 'clothing'}
    product3 = {'name': 'Novel', 'price': 15.00, 'category': 'books'}
    product4 = {'name': 'Unknown Item', 'price': 50.00, 'category': 'unknown'}

    print(f"Final price for {product1['name']}: ${main(product1):.2f}")
    print(f"Final price for {product2['name']}: ${main(product2):.2f}")
    print(f"Final price for {product3['name']}: ${main(product3):.2f}")
    print(f"Final price for {product4['name']}: ${main(product4):.2f}")
    # Output:
    # Electronics Discount: $100.00
    # Final price for Laptop: $900.00
    # Clothing Discount: $3.00
    # Final price for T-Shirt: $17.00
    # Book Discount: $0.75
    # Final price for Novel: $14.25
    # No discount available.
    # Final price for Unknown Item: $50.00