from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

from rpn.adapters.local_storage import LocalStorage
from rpn.domain.core import RPNController

app = FastAPI()


class StackModel(BaseModel):
    value: int

class OperatorModel(BaseModel):
    value: str

controller = RPNController(storage=LocalStorage())


@app.post("/rpn/stack/{stack_id}")
def apppend_value_to_stack(stack_id: str, stack: StackModel):
    stack = controller.append_value_to_stack(
        stack_id=stack_id, value=stack.value
    )

    if not stack:
        raise HTTPException(status_code=404, detail=f"Stack with id {stack_id} not found")
    
    return stack

@app.get("/rpn/stack/{stack_id}")
def get_stack_by_id(stack_id: str):
    stack = controller.read_stack(
        stack_id=stack_id
    )

    if not stack:
        raise HTTPException(status_code=404, detail=f"Stack with id {stack_id} not found")
    
    return stack


@app.post("/rpn/stack/{stack_id}/operator")
def apply_operator(stack_id: str, operator: OperatorModel):
    stack = controller.apply_operator_to_stack(stack_id=stack_id, operator=operator.value)

    if not stack:
        raise HTTPException(status_code=404, detail=f"Stack with id {stack_id} not found")
    
    return stack


@app.delete("/rpn/stack/{stack_id}")
def get_stack_by_id(stack_id: str):
    stack = controller.read_stack(
        stack_id=stack_id
    )

    if not stack:
        raise HTTPException(status_code=404, detail=f"Stack with id {stack_id} not found")

    controller.delete_stack(stack_id=stack_id)