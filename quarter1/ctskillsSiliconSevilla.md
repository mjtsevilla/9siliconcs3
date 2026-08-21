# Computational Thinking Exercise

## Smart School Canteen Queue

Name: Markie Jasmine
Section: Silicon
Last Name: Sevilla
Date: 8/21/26

## Step 1: Identify the Big Problem

#### Main Problem
The school canteen has a slow and crowded ordering process because students take too long to decide what to order, cashiers manually calculate totals and change, and there is no system for monitoring food inventory.

## Step 2: Identify the Sub-Problems:
1. Students take too long to decide what food to order.
2. The cashier takes too long to calculate the total cost and give the correct change.
3. There is no system for checking and tracking the available food items.
4. Long queues form because the ordering and payment process is slow.

## Step 3: Apply Computational Thinking Skills
|Sub-Problem|CT Skill|Proposed Solution|
|---|---|---|
|Students take too long to decide what to order.|Pattern Recognition|Display a digital menu with food names, prices, and available items so students can quickly choose.|
|Cashier takes too long to calculate totals and change.|Decomposition|Create a program that automatically calculates the total and change after the student selects their order and enters payment.|
|No system for checking food inventory.|Abstraction|Separate inventory into individual food items and track the quantity of each item.|
|Long queues form because the process is slow.|Pattern Recognition|Create an organized queue system where students are served in order and each completed transaction moves to the next student.|

## Step 4: Algorithmic Solution

### Selected Sub-Problem: Sub-Problem 2

START
INPUT number of food items
SET total = 0
FOR each food item:
    INPUT price
    INPUT quantity
    CALCULATE subtotal = price * quantity
    ADD subtotal to total
END FOR
DISPLAY total 
INPUT payment
IF payment >= total THEN
    CALCULATE change = payment - total
    DISPLAY change
    DISPLAY "Payment complete"
ELSE
    DISPLAY "Insufficient payment"
END IF 
END

