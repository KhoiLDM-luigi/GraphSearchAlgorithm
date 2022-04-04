# GraphSearchAlgorithm
This is a school project about graph (problem)searching in AI, containing Depth First Search, Breath First Search, Uniform Cost Search, A-star Search, Greedy Best First Search

Note: Graphical alogrithm presentation source code is not mine, only 'SearchAlgorithm.py' is mine

*program's command line argument*: Main.py \<test-case-file-path\> \<algorithm\> \<time-delay\>(optional)
  
+ \<algorithm\>: 'bfs' - Breath First Search; 'dfs' - Depth First Search, 'ucs' - Uniform Cost Search; 'astar' - A-star Search, 'greedy' - Greedy Best First Search
  
+ \<test-case-file-path\>: any text base input file, format as:
  
  ```
  <start-node> <end-node>
  <weighted-adjacency-matrix-of-the-graph>
  ``` 
  example is in file is 'input.txt' and 'input2.txt'
    
+ All searching algorithm return a first in first out type list of vistied node and path node

*addtional module*: pygame, matplotlib, numpy, networkx 
