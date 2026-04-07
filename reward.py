def calculate_reward(demand, solar, battery, grid):

    total_supply = solar + battery + grid

    demand_match = 1 - abs(demand - total_supply) / (demand + 1)

    renewable_ratio = (solar + battery) / (total_supply + 1)

    grid_penalty = grid / (demand + 1)

    reward = (
        0.5 * demand_match +
        0.4 * renewable_ratio -
        0.3 * grid_penalty
    )

    reward = max(0, min(1, reward))

    return reward
