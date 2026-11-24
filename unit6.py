"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

PROJECT: Thanksgiving Shopping List Manager

This program uses a Python dictionary to organize
Thanksgiving groceries and demonstrate common
hash table operations.

----------------------------------------------------
"""


def main():
    print("=== THANKSGIVING SHOPPING LIST MANAGER ===")

    # ===============================
    # CREATE A HASH TABLE
    # ===============================

    # Create an empty dictionary.
    # Grocery item names are the keys, and prices are the values.
    #
    # Python dictionaries behave like hash tables because
    # they use a hash function to locate information.
    # This allows us to quickly retrieve grocery prices
    # by searching for an item's name.

    shopping_list = {}

    # Add Thanksgiving grocery items.
    shopping_list["Turkey"] = 24.99
    shopping_list["Mashed Potatoes"] = 5.99
    shopping_list["Stuffing"] = 3.49
    shopping_list["Cranberry Sauce"] = 2.99
    shopping_list["Pumpkin Pie"] = 7.99
    shopping_list["Dinner Rolls"] = 4.50
    shopping_list["Green Beans"] = 3.25
    shopping_list["Gravy"] = 2.49

    print("\n=== INSERT OPERATIONS ===")

    print("Adding Thanksgiving groceries:")

    for item, price in shopping_list.items():
        print(f"{item}: ${price:.2f}")

    print(f"\nTotal grocery items: {len(shopping_list)}")


    # ===============================
    # LOOKUP OPERATIONS
    # ===============================

    print("\n=== LOOKUP OPERATIONS ===")

    # Dictionaries allow us to retrieve information
    # by searching for a specific key.

    print(f"Turkey costs: ${shopping_list['Turkey']:.2f}")
    print(f"Pumpkin Pie costs: ${shopping_list['Pumpkin Pie']:.2f}")


    # ===============================
    # UPDATE OPERATIONS
    # ===============================

    print("\n=== UPDATE OPERATIONS ===")

    print("Shopping list before updating:")
    print(shopping_list)

    # Assigning a new value to an existing key
    # replaces the previous value.

    shopping_list["Turkey"] = 29.99

    print("\nShopping list after updating Turkey's price:")
    print(shopping_list)

    print(f"Updated Turkey price: ${shopping_list['Turkey']:.2f}")


    # ===============================
    # DELETE OPERATIONS
    # ===============================

    print("\n=== DELETE OPERATIONS ===")

    print("Shopping list before deletion:")
    print(shopping_list)

    # The pop() method removes an item from the dictionary.

    shopping_list.pop("Gravy")

    print("\nShopping list after removing Gravy:")
    print(shopping_list)


    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # EDGE CASE 1: SEARCH FOR A MISSING ITEM

    print("\nEdge Case 1: Searching for an item that does not exist.")

    # The get() method prevents an error if the key is missing.

    item = shopping_list.get("Sweet Potato Casserole")

    if item is None:
        print("Sweet Potato Casserole was not found on the shopping list.")
    else:
        print(f"Sweet Potato Casserole costs: ${item:.2f}")


    # EDGE CASE 2: DELETE A MISSING ITEM

    print("\nEdge Case 2: Attempting to remove an item that does not exist.")

    # Providing a default value prevents an error
    # when trying to remove a missing key.

    removed_item = shopping_list.pop("Apple Pie", None)

    if removed_item is None:
        print("Apple Pie could not be removed because it was not on the list.")
    else:
        print("Apple Pie was successfully removed.")


    # EDGE CASE 3: EMPTY SHOPPING LIST

    print("\nEdge Case 3: Checking an empty shopping list.")

    empty_list = {}

    if not empty_list:
        print("The Thanksgiving shopping list is empty.")


    # ===============================
    # FINAL RESULTS
    # ===============================

    print("\n=== FINAL THANKSGIVING SHOPPING LIST ===")

    total_cost = 0

    for item, price in shopping_list.items():
        print(f"{item}: ${price:.2f}")
        total_cost += price

    print(f"\nTotal estimated cost: ${total_cost:.2f}")

    print(f"Total grocery items: {len(shopping_list)}")

    print("\n=== HAPPY THANKSGIVING! ===")


if __name__ == "__main__":
    main()
