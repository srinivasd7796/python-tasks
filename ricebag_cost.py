def rice_bag_cost(bags, cost, gross_wgt):
    # Calculate total weight, excluding one weight per bag (if that's the intent)
    total_weight = sum(bags) - len(bags)
    
    # Calculate the number of full bags and the remainder
    full_bags = total_weight // gross_wgt
    remaining_weight = total_weight - (full_bags * gross_wgt)
    
    # Final weight as a combination of full bags and the remainder as a fraction
    final_weight = full_bags + remaining_weight / 100
    
    # Cost per kilogram (adjusting for the weight of one bag)
    cost_per_kg = cost / (gross_wgt)
    
    # Total amount (cost for full bags + cost for remaining weight)
    total_cost = (full_bags * cost) + (remaining_weight * cost_per_kg)
    
    return total_cost, final_weight

# bags = [76, 83, 78, 67, 68, 64, 82, 76, 81, 75, 78, 69, 75, 69, 66, 70, 75, 73, 79, 79, 76, 79, 79, 79, 77, 73, 88, 78, 78, 74, 80, 67, 72, 76]
bags = []
cost = 1470  # Total cost for the weight
gross_wgt = 75  # Gross weight per bag (e.g., including bag weight)
amt, final_wgt = rice_bag_cost(bags, cost, gross_wgt)
print(f"Total Amount: {amt}")
print(f"Final Weight: {final_wgt}")
