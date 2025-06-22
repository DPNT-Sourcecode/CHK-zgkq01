
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name :str) -> str:
        if not isinstance(friend_name, str):
            raise ValueError(f" Friend Name : {friend_name} is not a string")

        return ("Hello World!")
