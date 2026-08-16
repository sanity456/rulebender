from __future__ import annotations
import json
import pytest
from fixtures.challenge import ACTION, GOAL, ILLEGAL, MAX_ATTEMPTS, RATIONALE, RULES, SUCCESS, TITLE
from tests.conftest import CONTRACT_PATH, DIRECT_SDK_VERSION

PROMPT = r"independent referee for a prose-rule exploitation game"


def test_success_scores_and_indexes(rulebender, direct_vm, direct_alice):
    direct_vm.mock_llm(PROMPT, json.dumps(SUCCESS))
    attempt_id = rulebender.play(ACTION, RATIONALE)
    attempt = rulebender.get_attempt(attempt_id)
    player = f"0x{bytes(direct_alice).hex()}"
    assert attempt["verdict"] == "LEGAL_SUCCESS"
    assert attempt["points"] == 3
    assert rulebender.get_player(player)["score"] == 3
    assert rulebender.get_attempt_count() == 1
    assert rulebender.get_attempt_id(0) == attempt_id
    assert rulebender.get_player_id(0) == player
    assert rulebender.get_stats()["legal_success"] == 1


def test_duplicate_content_rejected(rulebender, direct_vm):
    direct_vm.mock_llm(PROMPT, json.dumps(SUCCESS))
    rulebender.play(ACTION, RATIONALE)
    with direct_vm.expect_revert("duplicate_attempt_content"):
        rulebender.play(ACTION, RATIONALE)


def test_attempt_limit(direct_vm, direct_deploy, direct_alice):
    direct_vm.sender = direct_alice
    contract = direct_deploy(str(CONTRACT_PATH), TITLE, GOAL, RULES, 1, sdk_version=DIRECT_SDK_VERSION)
    direct_vm.mock_llm(PROMPT, json.dumps(ILLEGAL))
    contract.play(ACTION, RATIONALE)
    with direct_vm.expect_revert("player_attempt_limit_reached"):
        contract.play(ACTION + " Again.", RATIONALE + " This is a distinct explanation.")


def test_malformed_output_writes_nothing(rulebender, direct_vm):
    direct_vm.mock_llm(PROMPT, json.dumps({"verdict": "LEGAL_SUCCESS", "score": 3}))
    with direct_vm.expect_revert("[LLM_ERROR]"):
        rulebender.play(ACTION, RATIONALE)
    assert rulebender.get_attempt_count() == 0
    assert rulebender.get_player_count() == 0


def test_validator_replays_substance(rulebender, direct_vm):
    direct_vm.mock_llm(PROMPT, json.dumps(SUCCESS))
    rulebender.play(ACTION, RATIONALE)
    leader = direct_vm._captured_validators[-1][0]
    assert direct_vm.run_validator(leader_result=leader) is True
    direct_vm.clear_mocks()
    direct_vm.mock_llm(PROMPT, json.dumps(ILLEGAL))
    assert direct_vm.run_validator(leader_result=leader) is False
    assert direct_vm.run_validator(leader_error=RuntimeError("broken")) is False


def test_missing_and_index_views(rulebender, direct_vm):
    with direct_vm.expect_revert("attempt_not_found"):
        rulebender.get_attempt("missing")
    with direct_vm.expect_revert("attempt_index_out_of_bounds"):
        rulebender.get_attempt_id(0)
    with direct_vm.expect_revert("player_index_out_of_bounds"):
        rulebender.get_player_id(0)


@pytest.mark.parametrize(
    ("args", "message"),
    [
        (("x", GOAL, RULES, MAX_ATTEMPTS), "invalid_title"),
        ((TITLE, "short", RULES, MAX_ATTEMPTS), "invalid_goal"),
        ((TITLE, GOAL, "short", MAX_ATTEMPTS), "invalid_rules"),
        ((TITLE, GOAL, RULES, 0), "invalid_max_attempts"),
        ((TITLE, GOAL, RULES, 11), "invalid_max_attempts"),
    ],
)
def test_constructor_validation(direct_vm, direct_deploy, direct_alice, args, message):
    direct_vm.sender = direct_alice
    with direct_vm.expect_revert(message):
        direct_deploy(str(CONTRACT_PATH), *args, sdk_version=DIRECT_SDK_VERSION)
