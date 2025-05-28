# tests/integration/eidelon_response_flow_test.py
# Integration test for full Eidelon introspective response with triage scenario

import pytest
from src.eidelon.eidelon_core import invoke_eidelon

def test_invoke_eidelon_with_triage():
    response = invoke_eidelon("seer_beta", context="self_diagnostic", symbolic_plan=None)
    assert "user_id" in response
    assert "context" in response
    assert "flags" in response
    assert "council" in response
    assert "symbolic" in response
    assert "message" in response["message"]
    assert isinstance(response["message"], str)
