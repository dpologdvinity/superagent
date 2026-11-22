# What Does a Wish Leave Out?

Requirement recovery in wish-driven code agents. Columbia COMS 4705.

The milestone contract is [`paper/milestone/main.pdf`](paper/milestone/main.pdf), with source in
[`paper/milestone/main.tex`](paper/milestone/main.tex). The implementation is being rebuilt from
scratch to that design: Qwen3-8B AWQ on vLLM, a Qwen3-Embedding-0.6B five-label detector, and
~1,000 tasks (HumanEval+, MBPP+, BigCodeBench) with a 500/200/300 split and a 100-task pilot.
