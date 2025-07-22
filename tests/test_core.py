from rpn.adapters.local_storage import LocalStorage
from rpn.domain.core import RPNController


def test_append_value_to_stack():

    # Here we have already a local storage, when we use other adapters we can just test our application using this adapter
    controller = RPNController(storage=LocalStorage())
    result = controller.append_value_to_stack(stack_id="test", value=12)

    assert result.get("content") == [12]


def test_apply_operator_to_stack():

    # Here we have already a local storage, when we use other adapters we can just test our application using this adapter
    controller = RPNController(storage=LocalStorage())
    result = controller.append_value_to_stack(stack_id="test", value=12)
    result = controller.append_value_to_stack(stack_id="test", value=4)
    result = controller.apply_operator_to_stack(stack_id="test", operator="+")

    assert result.get("content") == [16]


def test_apply_operator_to_stack():

    # Here we have already a local storage, when we use other adapters we can just test our application using this adapter
    controller = RPNController(storage=LocalStorage())
    result = controller.append_value_to_stack(stack_id="test", value=12)
    result = controller.append_value_to_stack(stack_id="test", value=6)
    result = controller.append_value_to_stack(stack_id="test", value=3)
    result = controller.apply_operator_to_stack(stack_id="test", operator="/")

    assert result.get("content") == [12, 2]
