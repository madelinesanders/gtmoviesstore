from decimal import Decimal, ROUND_HALF_UP


def calculate_cart_total(cart, movies_in_cart):
    total = Decimal('0.00')  # Ensure total starts as a Decimal

    for movie in movies_in_cart:
        quantity = Decimal(cart.get(str(movie.id), 0))  # Convert quantity to Decimal
        price = Decimal(str(movie.price))  # Convert movie price safely to Decimal
        total += (price * quantity)  # Ensure multiplication stays precise

    return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)  # Rounds correctly to 2 decimal places
