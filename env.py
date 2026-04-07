import random
from reward import calculate_reward

class SmartEnergyEnv:

    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        self.max_steps = 5
        self.reset()

    def reset(self):

        self.time_step = 0

        if self.difficulty == "easy":
            self.energy_demand = 50
            self.solar_available = 40
            self.battery_level = 50

        elif self.difficulty == "medium":
            self.energy_demand = random.randint(40, 80)
            self.solar_available = random.randint(20, 60)
            self.battery_level = 50

        elif self.difficulty == "hard":
            self.energy_demand = random.randint(60, 120)
            self.solar_available = random.randint(10, 50)
            self.battery_level = random.randint(30, 70)

        return self.state()

    def step(self, action):

        solar_use = max(0, min(action.get("solar", 0), self.solar_available))
        battery_use = max(0, min(action.get("battery", 0), self.battery_level))
        grid_use = max(0, action.get("grid", 0))

        reward = calculate_reward(
            demand=self.energy_demand,
            solar=solar_use,
            battery=battery_use,
            grid=grid_use
        )

        self.battery_level -= battery_use
        self.time_step += 1

        done = self.time_step >= self.max_steps

        self.energy_demand = random.randint(40, 100)
        self.solar_available = random.randint(20, 60)

        return self.state(), reward, done, {}

    def state(self):

        return {
            "time_step": self.time_step,
            "energy_demand": self.energy_demand,
            "solar_available": self.solar_available,
            "battery_level": self.battery_level
        }
