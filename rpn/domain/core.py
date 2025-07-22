from rpn.ports.storage import StorageInterface


class RPNController:
    def __init__(
        self,
        storage: StorageInterface | None = None,
    ):
        self.storage = storage

    def append_value_to_stack(self, stack_id: str, value: float) -> dict:

        new_stack = self.storage.append_value(
            stack_id=stack_id, value=value
        )

        return new_stack

    def apply_operator_to_stack(self, stack_id: str, operator: str) -> dict:

        result = self.calculate(stack_id, operator)
        new_stack = self.append_value_to_stack(stack_id, result)
        return new_stack

    def read_stack(self, stack_id: str) -> dict | None:

        return self.storage.read_stack(stack_id=stack_id)


    def delete_stack(self, stack_id: str) -> None:

        self.storage.delete_stack(stack_id=stack_id)
    
    def calculate(self, stack_id: str, operator: str) -> float:
        try:
            second_operand = self.storage.pop_value(stack_id=stack_id)  # The last item in the stack is the second operator
            first_operand = self.storage.pop_value(stack_id=stack_id)
            equation = f"{first_operand} {operator} {second_operand}"
            return eval(equation)  # This can lead to remote code execution
        except Exception as ex:
            raise Exception("Error while calculating the stack")

