## Q.1_Answer Description

**1.a.** The subset of product of maximum total value such that the sum of their volumes is at most 15. 

   **Selected volumes are:5  3  4**

   **Total knapsack values: 34**

**1.b.** We solve this problem using Bottom-up Dynamic Programming method. Essentially we want to find maximum profit for every sub-array and possible capacity. This means            dp[i][c] will represent the maximum knapsack profit for capacity 'c' calculated from the first 'i' items.

   So, for each item at index 'i'(0<=i<item.lenght) and capacity 'c' (0<= c <= capacity), we have two options:

   1.Exclude the item at index 'i'. in the case, we will take whatever prifit we get form the sub-array excluding this item => dp[i-1][c]

   2.Include the item at index 'i' if it's weight is not more than capacity. In this case, we include its profit plus whatever profit we get form the remaining capacity and from      remaining => profit[i] + dp[i-1][c-weight[i]]

   Finally, our optimal solution will be the maximum of the above two values.

     dp[i][c] = max(dp[i-1][c], profit[i] + dp[i-1]-weight[i]])

 **The above solution has time and space complexity of O(N*C), where 'N' represents total items and 'C' us the maximum capacity.**


