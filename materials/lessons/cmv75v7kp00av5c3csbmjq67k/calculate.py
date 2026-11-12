"""Fictional workshop arithmetic only; no network, files or external action."""
from decimal import Decimal

def calculate(quantity=40, unit_price=Decimal("12"), rate=Decimal("0.10"), capacity=36):
    if quantity < 0 or capacity < 0 or unit_price < 0 or rate < 0:
        raise ValueError("Inputs must be nonnegative")
    subtotal = Decimal(quantity) * unit_price
    service = subtotal * rate
    return subtotal, service, subtotal + service, max(0, quantity - capacity)

if __name__ == "__main__":
    subtotal, service, total, gap = calculate()
    print(f"Subtotal: {subtotal:.2f} units")
    print(f"Service charge: {service:.2f} units")
    print(f"Meal-and-service total: {total:.2f} units")
    print(f"Seat shortfall: {gap}")
    print("Booking decision: PAUSE — availability, suitability and authorization unresolved")
