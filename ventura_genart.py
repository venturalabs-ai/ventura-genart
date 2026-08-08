from __future__ import annotations

from dataclasses import dataclass
import hashlib
import random


@dataclass(frozen=True)
class ArtConfig:
    width: int = 640
    height: int = 360
    circles: int = 12
    seed: str = "ventura"


def _seed_value(seed: str) -> int:
    return int.from_bytes(hashlib.sha256(seed.encode("utf-8")).digest()[:8], "big")


def generate_svg(config: ArtConfig) -> str:
    """Generate deterministic SVG artwork from a versionable seed/config."""
    if config.width <= 0 or config.height <= 0:
        raise ValueError("canvas dimensions must be positive")
    if not 1 <= config.circles <= 1000:
        raise ValueError("circles must be between 1 and 1000")
    rng = random.Random(_seed_value(config.seed))
    shapes: list[str] = []
    max_radius = max(2, min(config.width, config.height) // 8)
    for _ in range(config.circles):
        radius = rng.randint(2, max_radius)
        x = rng.randint(radius, max(radius, config.width - radius))
        y = rng.randint(radius, max(radius, config.height - radius))
        hue = rng.randint(0, 359)
        opacity = rng.randint(35, 90) / 100
        shapes.append(
            f'<circle cx="{x}" cy="{y}" r="{radius}" fill="hsl({hue} 70% 55%)" opacity="{opacity:.2f}" />'
        )
    body = "\n  ".join(shapes)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{config.width}" height="{config.height}" '
        f'viewBox="0 0 {config.width} {config.height}">\n  {body}\n</svg>\n'
    )


def fingerprint(svg: str) -> str:
    return hashlib.sha256(svg.encode("utf-8")).hexdigest()
