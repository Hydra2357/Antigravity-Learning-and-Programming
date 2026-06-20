"""
Competitive Analysis - The Ski Rental Problem
A classic online algorithm problem.
Problem:
- Buying skis costs B. Renting costs 1 per day.
- You do not know how many days N you will ski.
- Goal: Minimize total cost relative to the optimal offline cost (which knows N in advance).

Optimal Offline Cost:
- If N < B: Rent for N days (cost = N).
- If N >= B: Buy on Day 1 (cost = B).
- Cost_OPT = min(N, B).

Online Strategies:
1. Deterministic Strategy: Rent for B-1 days, and buy on Day B if you are still skiing.
   - Competitive ratio is guaranteed to be <= 2 - 1/B.
2. Randomized Strategy: Buy on Day j (where 1 <= j <= B) chosen randomly according to a probability distribution:
   - p_j = ((B - 1) / B)^(B - j) / (B * (1 - ((B - 1) / B)^B))
   - Expected competitive ratio converges to e / (e - 1) ~ 1.58.
"""

import random
import math

class SkiRentalSimulation:
    def __init__(self, buy_cost):
        self.B = buy_cost

    def get_optimal_offline_cost(self, n_days):
        return min(n_days, self.B)

    def run_deterministic_online(self, n_days):
        """Rent for B-1 days, buy on day B."""
        cost = 0
        for day in range(1, n_days + 1):
            if day < self.B:
                cost += 1  # Rent
            elif day == self.B:
                cost += self.B  # Buy
                break  # Bought, no more cost
        return cost

    def run_randomized_online(self, n_days):
        """
        Buy on day j (1 <= j <= B) chosen from the optimal randomized distribution.
        """
        # Calculate probability distribution for buying day j
        # p_j proportional to ((B-1)/B)^(B-j)
        probs = []
        for j in range(1, self.B + 1):
            p = ((self.B - 1) / self.B) ** (self.B - j)
            probs.append(p)
        
        total_prob = sum(probs)
        normalized_probs = [p / total_prob for p in probs]
        
        # Select buying day using the distribution
        buy_day = random.choices(range(1, self.B + 1), weights=normalized_probs, k=1)[0]
        
        # Calculate cost
        cost = 0
        for day in range(1, n_days + 1):
            if day < buy_day:
                cost += 1  # Rent
            elif day == buy_day:
                cost += self.B  # Buy
                break
        return cost

if __name__ == "__main__":
    print("=== Online Algorithms: Ski Rental Problem ===")
    
    B = 10  # Cost to buy skis
    print(f"Ski Purchase Cost (B): {B}")
    print(f"Renting Cost per day:  1")
    
    sim = SkiRentalSimulation(buy_cost=B)
    
    print(f"\n{'Days (N)':<10} | {'OPT Offline':<12} | {'Det Online':<12} | {'Det Ratio':<10} | {'Rand Online (Avg)':<18} | {'Rand Ratio':<10}")
    print("-" * 85)
    
    random.seed(42)
    trials = 5000
    
    for days in [2, 5, 9, 10, 15, 20]:
        opt_cost = sim.get_optimal_offline_cost(days)
        det_cost = sim.run_deterministic_online(days)
        det_ratio = det_cost / opt_cost
        
        # Run randomized strategy over trials to get expected cost
        rand_costs = [sim.run_randomized_online(days) for _ in range(trials)]
        avg_rand_cost = sum(rand_costs) / trials
        rand_ratio = avg_rand_cost / opt_cost
        
        print(f"{days:<10d} | {opt_cost:<12.1f} | {det_cost:<12.1f} | {det_ratio:<10.3f} | {avg_rand_cost:<18.3f} | {rand_ratio:<10.3f}")

    print("\nNote:")
    print(f"  - Max Deterministic Ratio: {2 - 1/B:.2f}x (Theoretical limit: 2.0x)")
    print(f"  - Max Randomized Ratio:    {1.58:.2f}x (Theoretical limit: e/(e-1) ~ 1.58x)")
