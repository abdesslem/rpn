from rpn.ports.storage import StorageInterface


class LocalStorage(StorageInterface):
    def __init__(self):
        self.stacks = [
            {
                "stack_id": "test",
                "content": []
            },
            {
                "stack_id": "test1",
                "content": []
            }
        ]

    def append_value(self, stack_id: str, value: float) -> dict | None:
        for stack in self.stacks:
            if stack_id == stack.get("stack_id"):
                stack.get("content").append(value)
                return stack

    def pop_value(self, stack_id: str) -> float | None:
        for stack in self.stacks:
            if stack_id == stack.get("stack_id"):
                return stack.get("content").pop()

    def read_stack(self, stack_id: str) -> dict | None:
        for stack in self.stacks:
            if stack_id == stack.get("stack_id"):
                return stack

    def delete_stack(self, stack_id: str) -> None:
        self.stacks = [item for item in self.stacks if item.get("stack_id") != stack_id]
