IMPLICIT_CHECK_PATTERNS = {

    "duration": [

        "for months",

        "for years",

        "for weeks",

        "for a while",

        "lately",

        "recently"
    ],

    "severity": [

        "overwhelming",

        "really hard",

        "intense",

        "draining",

        "exhausting"
    ],

    "functional_impact": [

        "can't focus",

        "can't function",

        "can't work",

        "can't study",

        "everything feels difficult"
    ],

    "support_quality": [

        "nobody understands",

        "no one to talk to",

        "feel alone",

        "disconnected"
    ],

    "withdrawal_level": [

        "avoiding people",

        "isolating",

        "stopped talking",

        "pulling away"
    ],

    "hopelessness": [

        "nothing matters",

        "pointless",

        "don't look forward to anything",

        "empty"
    ],

    "passive_ideation": [

        "tired of everything",

        "don't want to deal with this",

        "wish I could disappear"
    ]
}


def infer_covered_checks(message):

    message_lower = message.lower()

    inferred_checks = []

    for check, patterns in (
        IMPLICIT_CHECK_PATTERNS.items()
    ):

        for pattern in patterns:

            if pattern in message_lower:

                inferred_checks.append(
                    check
                )

                break

    return inferred_checks