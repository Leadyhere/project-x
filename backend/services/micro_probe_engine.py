import random

from data.micro_probes import (
    MICRO_PROBES
)


def select_micro_probe(session):

    used_probes = [

        item["probe"]

        for item
        in session.probe_memory
    ]

    available = [

        probe

        for probe
        in MICRO_PROBES

        if probe not in used_probes
    ]

    if not available:
        return None

    return random.choice(
        available
    )