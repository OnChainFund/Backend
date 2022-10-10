from strawberry import StrawberryField

class MyCustomField(StrawberryField):
    def get_type(self) -> Type:
		type_ = super().get_type()
        # Modify type
		return type_

    def get_arguments(self) -> Dict[str, Type]:
		arguments = super().get_arguments()
        # Modify arguments
		return arguments

    def get_result(self, source: Any, info: Info, arguments: Dict[str, Any]) -> Union[Awaitable[Any], Any]:
		result = super().get_result(source, info, arguments)
        # Modify result
		return result