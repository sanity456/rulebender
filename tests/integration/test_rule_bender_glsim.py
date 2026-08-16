from __future__ import annotations
import json
from pathlib import Path
from gltest import get_contract_factory, get_validator_factory
from gltest.assertions import tx_execution_succeeded
from gltest.types import TransactionStatus
from gltest.utils import extract_contract_address
from fixtures.challenge import ACTION, GOAL, MAX_ATTEMPTS, RATIONALE, RULES, SUCCESS, TITLE

PROMPT = "independent referee for a prose-rule exploitation game"


def test_five_validator_attempt():
    validators = get_validator_factory().batch_create_mock_validators(5, mock_llm_response={"nondet_exec_prompt": {PROMPT: json.dumps(SUCCESS)}})
    context = {"validators": [validator.to_dict() for validator in validators]}
    path = Path(__file__).resolve().parents[2] / "contracts" / "rule_bender.py"
    factory = get_contract_factory(contract_file_path=path)
    receipt = factory.deploy_contract_tx(args=[TITLE, GOAL, RULES, MAX_ATTEMPTS], wait_transaction_status=TransactionStatus.FINALIZED)
    assert tx_execution_succeeded(receipt)
    contract = factory.build_contract(extract_contract_address(receipt))
    played = contract.play(args=[ACTION, RATIONALE]).transact(transaction_context=context, wait_transaction_status=TransactionStatus.FINALIZED)
    assert tx_execution_succeeded(played)
    assert contract.get_stats(args=[]).call()["legal_success"] == 1
