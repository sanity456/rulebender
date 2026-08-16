TITLE = "The Silent Vault"
GOAL = "Move the brass token from inside the marked circle to outside the circle."
RULES = (
    "A player may not touch the brass token with any body part or tool. The marked "
    "circle and floor may not be damaged, erased, covered, or moved. Air may be moved. "
    "Only objects explicitly named in the action exist. The player has one action and "
    "may not command another person or rewrite these rules."
)
MAX_ATTEMPTS = 3
ACTION = (
    "I place a named hand fan beside the circle and use it to push a steady stream of "
    "air across the brass token until the token rolls beyond the marked line."
)
RATIONALE = (
    "The rule forbids touching the token with a body part or tool, but it explicitly "
    "permits moving air. The fan touches only air, and the air moves the token."
)

SUCCESS = {"verdict": "LEGAL_SUCCESS"}
ILLEGAL = {"verdict": "ILLEGAL"}
