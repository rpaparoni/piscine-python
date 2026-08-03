from typing import List, Dict, Any


def artifact_sorter(artifacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(artifacts, key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell['name']} *", spells))


def mage_stats(mages: List[Dict[str, Any]]) -> Dict[str, Any]:

    max_power = max(mages, key=lambda mage: mage['power'])['power']
    min_power = min(mages, key=lambda mage: mage['power'])['power']
    all_powers = list(map(lambda mage: mage['power'], mages))
    avg_power = round(sum(all_powers) / len(all_powers), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Earth Shield', 'power': 96, 'type': 'relic'},
        {'name': 'Shadow Blade', 'power': 75, 'type': 'weapon'},
        {'name': 'Shadow Blade', 'power': 107, 'type': 'relic'},
        {'name': 'Storm Crown', 'power': 95, 'type': 'armor'}]

    print("\nTesting artifact sorter...")
    print(f"{artifact_sorter(artifacts)}")
    print("\nTesting artifact min power...")
    print(f"{power_filter(artifacts, 100)}")
    print("\nTesting spell transformer..")
    print(f"{spell_transformer(artifacts)}")
    print("\nTesting mage stats..")
    print(f"{mage_stats(artifacts)}")
