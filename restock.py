def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a given current day. It will also return "available_items".
    '''

    # This is creating a list for the restocking days by using a step range
    restocking_days = list(range(0, 50, 7))
    
    #This checks whether the current day comes across a restocking day by going through the restock day list
    if current_day in restocking_days:
        restocked_units = 2000 - available_items # Checks for the units required for 2000
        available_items += restocked_units # This updates available stock after restocking
    else:
        restocked_units = 0 # No restocks for non-restock days
    
    # This adds the data for the current day
    inventory_records.append([current_day, 0, restocked_units, available_items])

   

    
    return available_items
