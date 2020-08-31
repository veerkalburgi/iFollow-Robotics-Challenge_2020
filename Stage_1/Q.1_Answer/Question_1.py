#!/usr/bin/env python



from __future__ import print_function

def knapsack(values,volumes,capacity):
    #basic checks
    n = len(values)
    if capacity <= 0 or n==0 or len(volumes) !=n:
        return 0
    
    dp= [[0 for x in range(capacity+1)]for y in range(n)]
    
    #populate the capacity =0 coloums, with '0' capacity we have '0' values
    for i in range(0,n):
        dp[i][0] =0
    
    for c in range(0,capacity+1):
        if volumes[0] <= c:
            dp[0][c] = values[0]
    
    # process all sub-arrays for all the capacities
    for i in range(1,n):
        for c in range(1,capacity+1):
            value1, value2 = 0, 0
            #include the item, if it is not more than the capacity
            if volumes[i] <= c:
                value1 = values[i] + dp[i-1][c - volumes[i]]
            #exclude the item
            value2 = dp[i-1][c]
            #take maximum
            dp[i][c] =max(value1, value2)
    
    print_selected_elements(dp,volumes, values, capacity)
    #maximum profit will be at the bottom-right corner.
    return dp[n-1][capacity]

def print_selected_elements(dp,volumes,values,capacity):
    print("Selected volumes are:", end= '')
    n =len(volumes)
    totalvalue = dp[n-1][capacity]
    for i in range(n-1, 0, -1):
        if totalvalue != dp[i-1][capacity]:
            print(str(volumes[i]) + " ",end=" ")
            capacity -=volumes[i]
            totalvalue -=values[i]
    

def main():
    print("Total knapsack values: " +
        str(knapsack([7,9,5,12,14,6,12], [3,4,2,6,7,3,5], 15)))


main()