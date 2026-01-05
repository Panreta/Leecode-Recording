“tractable”: P class

• If there exists an algorithm that solves it (of course).

• And its worst case running time is 𝑂(𝑛^𝑘) for some constant 𝑘 on inputs of size 𝑛


An **alphabet** Σ is a finite set of symbols.
A **language** 𝐿 over Σ is any set of strings made up of symbols from Σ.

The language of all strings over Σ (sometimes called universe) is denoted by Σ∗

Every language 𝐿 over Σ is a subset of Σ∗


![[Pasted image 20251204215730.png]]


# Complex Class P
𝑃 = {𝐿: 𝐿 is decided by a polynomial-time algorithm}

# Complex Class NP

- NP is the set of decision problems _solvable_ in polynomial time by a [nondeterministic Turing machine](https://en.wikipedia.org/wiki/Nondeterministic_Turing_machine "Nondeterministic Turing machine").

- NP is the set of decision problems _verifiable_ in polynomial time by a [deterministic Turing machine](https://en.wikipedia.org/wiki/Deterministic_Turing_machine "Deterministic Turing machine").

### Example 1:HAM-CYCLE check if Hamiltonian cycle

# NP-Completeness
$L_1<L_2$: $if\space x\in L_1, f(x) \in L_2$  

![[Pasted image 20251205125315.png]]

### Example 1: Boolean circuit
![[Pasted image 20251207174129.png]]