### Kadane's algorithm
*So we assume that the largest subarray is the first element, then we go through A[1:] elements (all elements except the first one).

At each step, what we do is:

Can current element plus the last largest sum_ help to find a largest subarray (line 4)?
If yes, update the max_ending_here or our local maximum, otherwise current element is the largest subarray (array of one).
Then update the global maximum or max_so_far if there is a new global maximum.
