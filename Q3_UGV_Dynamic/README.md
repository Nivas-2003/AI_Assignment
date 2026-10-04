\# Q3 - UGV Dynamic Obstacle Navigation



\## Aim



To implement A\* Search with dynamic replanning for UGV navigation in a changing environment.



\## Algorithm



A\* Search with Dynamic Replanning



\## Grid Size



30 × 30



\## Working



The UGV moves toward the goal using A\*. When a new obstacle appears on the current path, the obstacle is detected and a new path is calculated.



\## Process



1\. Start navigation

2\. Find path using A\*

3\. Move toward the goal

4\. Detect new obstacle

5\. Replan the path

6\. Continue navigation

7\. Reach the goal



\## Measurements



\- Total steps

\- Dynamic obstacles

\- Number of replanning operations

\- Cells explored

\- Execution time

\- Mission status



\## File



`q3\_ugv\_dynamic.py`



\## Conclusion



A\* with dynamic replanning successfully allows the UGV to adapt to newly appearing obstacles and reach the destination.

