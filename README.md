# Dynathink
This is a repository for the code of paper: [DynaThink: Fast or Slow? A Dynamic Decision-Making Framework for Large Language Models](https://arxiv.org/abs/2407.01009)

We provide data of 3 datasets including both few shot and zero shot.

The two main files for the main results are `Dynathink.py` and `Dynathink_iterative.py`. Because the iterative version doesn't add a lot more fast set answers. You can directly use the former one.

To run the files, you just need to fill in the datapath.
If you want to use your own data, you have to follow the same data format as our examples'. We generate these data thanks to the code from https://github.com/NingMiao/SelfCheck. We use its first two steps to generate answers and divide steps.
The ablation study part is not complete, we will update it soon.
