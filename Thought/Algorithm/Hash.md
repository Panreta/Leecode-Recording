• Hash function

• ℎ: 𝑈 → {0, 1, … , 𝑚 - 1}

# Chaining

h(k) = k % 7

0: 42
1: 71
2: 23 -> 51 -> 9
3: 10 
4: / 
5: / 
6: /

Worst: Θ(𝑛)
unsuccessful search is Θ(1 + 𝛼)


## Division Method

ℎ(k) = 𝑘 mod 𝑚 (𝑘 % 𝑚).

Avoid m to be prime. I think it is because h(k) is a mapping $\mathbb{N} \rightarrow \mathbb{Z}_m$ , and in Lagrange Theorem $\mathbb{Z}_m$ can be splitted into small orbits if m is not prime number, like $\mathbb{Z}_6$ if you are the multiple of 2, you will only pile on the position {0,2,4}, which is the orbit.

So m is prime for avoiding hash collision, which is 2 or more elements map to one position. And also, m can't be $2^p - 1$ even though it has a high change to produce prime number($2^p - 1$ is not prime iff $p = 2^k,k \in \mathbb{N}$)  for the following reason

$R = 2^p$ and $m = 2^p - 1$:

$$k \pmod m = (c_n R^n + \dots + c_1 R^1 + c_0) \pmod m$$

Substitute $R = 1$:

$$k \pmod m = (c_n (1)^n + \dots + c_1 (1) + c_0) \pmod m$$

$$k \pmod m = (c_n + \dots + c_1 + c_0) \pmod m$$

## Multiplication
$h(k) = \lfloor m(kA - \lfloor kA \rfloor) \rfloor$ ,
Advantage: 𝑚 can be any number, even a power of 2, so prime number is not an issue now.

---
# Universal Hashing

### Motivation: The Vulnerability of Fixed Hashing

- **The Problem:** If a hash function is fixed and known, a malicious adversary can easily exploit it.
    
- **Worst Case:** An adversary can engineer keys to cause worst-case degeneration, where all keys hash into the same slot.
    
- **The Solution:** One should be able to select a different hash function for each usage rather than relying on a single fixed one.
    

### Definition: Universal Set of Hash Functions

A set of hash functions, denoted as $\mathcal{H}$, is considered **universal** if it satisfies the following condition:

- For every pair of distinct keys $k, l \in U$, the number of hash functions $h \in \mathcal{H}$ that cause a collision ($h(k) = h(l)$) is at most $|\mathcal{H}|/m$.
    
    - _Note: This implies the probability of a collision is $\leq 1/m$._
        

### A Good Universal Family of Functions

A standard example of a universal set of hash functions is defined by the formula:

$$h_{ab}(k) = ((ak + b) \pmod p) \pmod m$$

**Where:**

- $p$ is a prime number.
    
- $a \in \{1, 2, ..., p-1\}$ (a random integer excluding 0).
    
- $b \in \{0, 1, 2, ..., p-1\}$ (a random integer).
    

### Performance and Further Reading

- **Expected Complexity:** Universal hashing yields an average-case performance of $O(1 + \alpha)$.
    
- **Reference:** Refer to **CLRS 11.3.3** (Introduction to Algorithms) for:
    
    1. The proof of why the function family above is universal.
        
    2. The derivation of the $O(1 + \alpha)$ complexity.

---

# Open Addressing

Open addressing is feasible only when the loading factor α is less than or equal to 1.

Linear Probing: ℎ(𝑘, 𝑖 )= (h'(k) + 𝑖 ) % 𝑚.
Drawback: Linear Probing suffers from “primary clustering” issue.

• # probes goes up pretty quickly as 𝛼 (= 𝑛/𝑚) approaches 1 due to cluster

like ℎ(𝑘, 11 )= (h'(k) + 𝑖 ) % 11 to 22, 33, 44, 55.

forming from previous insertions

Quadratic Probing: h(k, i) = (h'(k) + c₁i + c₂i²) % m, also “secondary clustering”

Double Hashing: $h(k, i) = (h_1(k) + i \cdot h_2(k)) \bmod m$ 
