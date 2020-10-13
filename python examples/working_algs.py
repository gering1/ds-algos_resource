    def minPathSum(self, grid):https://leetcode.com/problems/minimum-path-sum/
        """
        :type grid: List[List[int]]
        :rtype: int
        dp
        you can only go down or right at any time
        
        """
        m = len(grid)-1
        n = len(grid[0])-1
        dp = [[0 for i in range(len(grid[0]))]for j in range(len(grid))]
        localSum = 0
        for i in range(len(dp)):
            localSum += grid[i][0]
            dp[i][0] = localSum
        
        localSum = dp[0][0]
        for i in range(1,len(dp[0])):
            localSum += grid[0][i]
            dp[0][i] += localSum
            
        for i in range(1,len(dp)):
            for j in range(1,len(dp[i])):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[m][n]
def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in range(1,len(nums)):
            if not nums[pointer] and nums[i]:
                nums[pointer],nums[i] = nums[i],nums[pointer]
                pointer += 1
            if nums[pointer]:
                pointer += 1
        return nums
                    
class MinStack(object):https://leetcode.com/problems/min-stack/

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append((x,min(x,self.getMin())))
        

    def pop(self):
        """
        :rtype: None
        """
        self.items.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.items:
            return self.items[-1][1]
        return float('inf') 
def invertTree(self, root): https://leetcode.com/problems/invert-binary-tree/
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            node.left,node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root

def inorderTraversal(self, root):
    ans = []
    stack = []
    
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            ans.append(tmpNode.val)
            root = tmpNode.right
        
    return ans


def stringProcess(num):
    """
    A -> 1
    AA -> 1
    AZ -> 
    """
def preorderTraversal(self,root):
    """
    while loop
        if the value exists
        add the node... add the left and right nodes
        stack pops off end... so add right then left (preorder is root->left-> right)
    
    """
    res = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res
    
    <!--Number of Islands-->
<section  class = "data-struct" id = "number-islands">
    <div class = "container">
        <h2 class= "data-title">Number of Islands</h2>   
        <div class = "box">
        <a href = "https://leetcode.com/problems/number-of-islands/submissions/" target = "_blank">Link To Problem</a>
        <p class = "code-block" style =  "white-space: pre">def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                self.dfs(grid,i,j)
                count += 1
    return count

    def dfs(self,grid,x,y):
    #check if x or y index is out of bounds or if current location is not a "1"
    if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0 or grid[x][y] != "1": 
        return 
    else:

        grid[x][y] = "." #mark current location so it doesn't get counted again
        <i class="comment">#check neighbors</i>
        self.dfs(grid,x+1,y)
        self.dfs(grid,x-1,y)
        self.dfs(grid,x,y+1)
        self.dfs(grid,x,y-1)
  <p>This is a popular graph traversal problem. A DFS is one way to solve this problem. The idea is to traverse the graph, and if the current value is "1", then call a dfs on the current location. 
      The dfs marks the current value as seen with "." so it isn't reached again, then checks each neighbor's value with a recursive call. This will mark each connected 1 as ".", and 
      stop when there is no longer any available space on the island. After the recursion is done on the initial location, you know that the whole island has been scanned, so you can add one to the 
      count of islands.     
  
  </p>
  </div>
  
  </section>

  <!--Number of Islands-->
<section  class = "data-struct" id = "merge-intervals">
    <div class = "container">
        <h2 class= "data-title">Merge Intervals</h2>   
        <div class = "box">
        <a href = "https://leetcode.com/problems/number-of-islands/submissions/" target = "_blank">Link To Problem</a>
        <p class = "code-block" style =  "white-space: pre">def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    res = []
    for i in sorted(intervals, key = lambda i:i[0]): <i class="comment"></i>#sort by starting number </i>
    <i class="comment">#check if interval is not the first interval and current first number is overlapped by previous second letter</i>
        if res and i[0] <= res[-1][1]: 
        <i class="comment">#curr end could be less than previous end, so assign end the larger of the two</i>
            res[-1][1] = max(res[-1][1],i[1]) 
        else:
            res.append([i[0],i[1]])
    return res<p>
  This problem has a bit of a trick to make it much easier. If the intervals are sorted, you can use a list to keep a resulting list of intervals in order. Iterating through the sorted intervals,
  you can simply compare the interval to the last interval in the resulting list of intervals, and compare the current first value to the last items last value. If the first value is larger, there
  is a need to merge the intervals. If not, the interval needs to be added as a separate interval to the resulting list. The only exception is the first interval, which needs to be added because there is 
  nothing before it to overlap with.
  </p>
  </div>
  
  </section>
  
  
  <!--Subarray Sum Equals K-->
<section  class = "data-struct" id = "subarray-sum">
    <div class = "container">
        <h2 class= "data-title">Subarray Sum Equals K</h2>   
        <div class = "box">
        <a href = "https://leetcode.com/problems/subarray-sum-equals-k/" target = "_blank">Link To Problem</a>
        <p class = "code-block" style =  "white-space: pre">def subarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    
    running_counts = dict()
    running_counts[0] = 1
    sums = 0
    res = 0
    for i in nums:
        sums += i
        res += running_counts.get(sums-k,0)
        running_counts[sums] = running_counts.get(sums,0) + 1
    return res<p>
  
  </p>
  </div>
  
  </section>

    <!--Copy List With Random Pointer-->
<section  class = "data-struct" id = "copy-list-random-pointer ">
    <div class = "container">
        <h2 class= "data-title">Copy List With Random Pointer</h2>   
        <div class = "box">
        <a href = "https://leetcode.com/problems/subarray-sum-equals-k/" target = "_blank">Link To Problem</a>
        <p class = "code-block" style =  "white-space: pre">def subarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    
    running_counts = dict()
    running_counts[0] = 1
    sums = 0
    res = 0
    for i in nums:
        sums += i
        res += running_counts.get(sums-k,0)
        running_counts[sums] = running_counts.get(sums,0) + 1
    return res<p>
  
  </p>
  </div>
  
  </section>

      <!--Squares of a Sorted Array-->
<section  class = "data-struct" id = "sorted-arr-squares ">
    <div class = "container">
        <h2 class= "data-title">Squares of a Sorted Array</h2>   
        <div class = "box">
        <a href = "https://leetcode.com/problems/squares-of-a-sorted-array/" target = "_blank">Link To Problem</a>
        <p class = "code-block" style =  "white-space: pre">def sortedSquares(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    
    """
    res = [0]*len(A)
    l,r = 0,len(A)-1
    count = 0
    while l <= r:
        l_square,r_square = A[l] ** 2, A[r] ** 2
        if l_square >= r_square:
            res[-1-count] = l_square
            l+=1
        else:
            res[-1-count] = r_square
            r -= 1
        count += 1
            
    return res<p>
    The only problem to handle is with negative numbers. This can be dealt with using a 
    two pointer approach. Comparing each pointer, we choose the larger one to put into the           
    last available index of the result list. We start at the beginning and end because the 
    the largest negative squares are at the start.
  </p>
  </div>
  
  </section>





<!--Squares of a Sorted Array-->
<section  class = "data-struct" id = "one-bits ">
<div class = "container">
  <h2 class= "data-title">Number of One Bits</h2>   
  <div class = "box">
  <a href = "https://leetcode.com/problems/number-of-1-bits/" target = "_blank">Link To Problem</a>
  <p class = "code-block" style =  "white-space: pre">def hammingWeight(self, n):
"""
:type n: int
:rtype: int
"""
count = 0
while n != 0:
    n &= (n-1) # n-1 is the flips the zeros until the least significant one in n so it will remove the least significant 1 by anding it (the lsb in n + first 0 in n-1 )
    count += 1
return count
          
<p>

</p>
</div>

</section>




<!--Squares of a Sorted Array-->
<section  class = "data-struct" id = "one-bits ">
    <div class = "container">
      <h2 class= "data-title">Climbing Stairs</h2>   
      <div class = "box">
      <a href = "https://leetcode.com/problems/climbing-stairs/" target = "_blank">Link To Problem</a>
      <p class = "code-block" style =  "white-space: pre">def climbStairs(self, n):
        
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*n
        dp[0] = 1
        if len(dp) <= 1:
            return dp[-1]
        dp[1] = 2
        
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
              
    <p>
    
    </p>
    </div>
    
    </section>