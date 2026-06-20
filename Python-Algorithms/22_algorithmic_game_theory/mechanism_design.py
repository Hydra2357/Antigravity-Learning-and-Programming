"""
Algorithmic Game Theory and Mechanism Design
Includes:
1. Vickrey Auction (Second-Price Sealed-Bid Auction):
   - A game-theoretic auction mechanism where bidders submit sealed bids.
   - The highest bidder wins but pays the second-highest bid.
   - Proves truth-telling (bidding one's exact valuation) is a dominant strategy.
2. Gale-Shapley Stable Marriage Algorithm:
   - Solves the stable matching problem between two sets of agents (e.g. proposers and acceptors) with preferences.
   - Time Complexity: O(N^2) where N is the size of each group.
"""

# --- 1. Vickrey Auction ---
def run_vickrey_auction(bids):
    """
    bids: dict mapping bidder names to bid amounts.
    Returns: (winner, price_paid)
    """
    if not bids:
        return None, 0
    if len(bids) == 1:
        winner = list(bids.keys())[0]
        return winner, bids[winner]
        
    # Sort bids in descending order
    sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)
    
    winner, highest_bid = sorted_bids[0]
    _, second_highest_bid = sorted_bids[1]
    
    return winner, second_highest_bid

# --- 2. Gale-Shapley Stable Marriage ---
def stable_matching(proposers, acceptors, proposer_prefs, acceptor_prefs):
    """
    proposers: list of proposer IDs
    acceptors: list of acceptor IDs
    proposer_prefs: dict mapping proposer ID to list of acceptor IDs in preferred order
    acceptor_prefs: dict mapping acceptor ID to list of proposer IDs in preferred order
    
    Returns: dict mapping proposer -> matched acceptor
    """
    # Inverse map of acceptor preferences for constant time lookups
    # rank[acceptor][proposer] = index of proposer in acceptor's preference list
    acceptor_rank = {acc: {prop: idx for idx, prop in enumerate(prefs)} 
                     for acc, prefs in acceptor_prefs.items()}
                     
    # Matchings: proposer -> acceptor and acceptor -> proposer
    prop_matched = {p: None for p in proposers}
    acc_matched = {a: None for a in acceptors}
    
    # Track which preference index the proposer should try next
    next_proposal = {p: 0 for p in proposers}
    
    # Free proposers queue
    free_proposers = list(proposers)
    
    while free_proposers:
        p = free_proposers.pop(0)
        
        # Get next preferred acceptor for proposer p
        pref_list = proposer_prefs[p]
        a = pref_list[next_proposal[p]]
        next_proposal[p] += 1
        
        current_match = acc_matched[a]
        if current_match is None:
            # Acceptor is free: match p and a
            acc_matched[a] = p
            prop_matched[p] = a
        else:
            # Acceptor is matched: compare p with current_match
            # Lower rank index means higher preference
            if acceptor_rank[a][p] < acceptor_rank[a][current_match]:
                # Acceptor prefers p over current_match: break old match, match p and a
                prop_matched[current_match] = None
                free_proposers.append(current_match)
                
                acc_matched[a] = p
                prop_matched[p] = a
            else:
                # Acceptor rejects p: p remains free
                free_proposers.append(p)
                
    return prop_matched

if __name__ == "__main__":
    print("=== Mechanism Design & Game Theory Demo ===")
    
    # 1. Vickrey Auction
    print("\n1. Second-Price Sealed-Bid (Vickrey) Auction:")
    bids = {
        "Alice": 120,   # Alice's valuation is 120
        "Bob": 150,     # Bob's valuation is 150
        "Charlie": 90,  # Charlie's valuation is 90
        "Diana": 110    # Diana's valuation is 110
    }
    print(f"  Submitted Bids: {bids}")
    winner, price = run_vickrey_auction(bids)
    print(f"  Winner: {winner} | Price Paid: {price} (Expected Winner: Bob, Price: 120)")
    print("  Note: Bob wins because he bid highest (150), but only pays Alice's bid (120).")
    
    # 2. Gale-Shapley Stable Marriage
    print("\n2. Gale-Shapley Stable Marriage:")
    # Proposers (Men) and Acceptors (Women)
    men = ['M1', 'M2', 'M3']
    women = ['W1', 'W2', 'W3']
    
    # Preferences (ordered best to worst)
    men_prefs = {
        'M1': ['W1', 'W2', 'W3'],
        'M2': ['W2', 'W1', 'W3'],
        'M3': ['W1', 'W2', 'W3']
    }
    
    women_prefs = {
        'W1': ['M2', 'M1', 'M3'],
        'W2': ['M1', 'M2', 'M3'],
        'W3': ['M1', 'M2', 'M3']
    }
    
    matches = stable_matching(men, women, men_prefs, women_prefs)
    print("  Stable Matches (Proposer -> Match):")
    for proposer, partner in matches.items():
        print(f"    {proposer} <---> {partner}")
