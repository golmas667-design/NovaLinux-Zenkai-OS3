#!/usr/bin/python3
"""Small, dependency-free hardware temperature reader for NovaLinux."""
from pathlib import Path

def read_temperatures():
    values = []
    for path in sorted(Path("/sys/class/thermal").glob("thermal_zone*/temp")):
        try:
            raw = int(path.read_text().strip())
            if 0 < raw < 200000:
                zone = path.parent / "type"
                name = zone.read_text().strip() if zone.exists() else "Thermal"
                values.append(f"{name}: {raw / 1000:.0f}°C")
        except (OSError, ValueError):
            pass
    if not values:
        for path in sorted(Path("/sys/class/hwmon").glob("hwmon*/temp*_input")):
            try:
                raw = int(path.read_text().strip())
                if 0 < raw < 200000:
                    values.append(f"{path.parent.name}: {raw / 1000:.0f}°C")
            except (OSError, ValueError):
                pass
    return values[:4]

temps = read_temperatures()
print("  |  ".join(temps) if temps else "Temperatura: sensor no disponible")
