# Expected checks

The baseline arithmetic is 40 × 12 = 480 units; 10% of 480 = 48 units; 480 + 48 = 528 units. The generated 480 is a supported subtotal but an incorrect final meal-and-service total. Seat gap: 40 − 36 = 4. Availability and authorization remain unresolved. No contact, booking or purchase has happened.

`python3 calculate.py` should print exactly:

```text
Subtotal: 480.00 units
Service charge: 48.00 units
Meal-and-service total: 528.00 units
Seat shortfall: 4
Booking decision: PAUSE — availability, suitability and authorization unresolved
```

Execution of this code is arithmetic evidence only. It cannot independently confirm source values or real venue conditions. If Python is unavailable, use the calculator steps in worksheet.md. No Python installation is required to complete the learning exercise.
