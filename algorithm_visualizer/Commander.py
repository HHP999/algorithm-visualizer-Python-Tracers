import json
import random
import string
import sys
import atexit


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        # 你可以根据需要自定义序列化方式
        if hasattr(obj, 'key'):
            return obj.key
        return f"{obj.__class__.__name__}"

class Commander:
    MAX_COMMANDS = 1000000
    MAX_OBJECTS = 100
    key_randomizer = random.Random()
    key_length = 8
    object_count = 0
    commands = []

    class Command:
        def __init__(self, key, method, args):
            self.args = args
            self.key = key
            self.method = method

    @staticmethod
    def command_(key, method, args):
        # 如果不是 list 或 tuple，就强制转成 list
        if not isinstance(args, (list, tuple)):
            args = [args]

        commands_data = json.dumps(args, cls=CustomEncoder)
        parsed_args = json.loads(commands_data)
        Commander.commands.append(Commander.Command(key, method, parsed_args))
        
        if len(Commander.commands) > Commander.MAX_COMMANDS:
            raise Exception("Too Many Commands")
        if Commander.object_count > Commander.MAX_OBJECTS:
            raise Exception("Too Many Objects")


    def __init__(self, args):
        Commander.object_count += 1
        self.key = ''.join(random.choices(string.ascii_lowercase + string.digits, k=Commander.key_length))
        class_name = self.__class__.__name__
        self.command(class_name, args)

    def destroy(self):
        Commander.object_count -= 1
        self.command("destroy", [])

    def command(self, method, args):
        Commander.command_(self.key, method, args)

    @staticmethod
    def save_commands():
        try:
            content = json.dumps([command.__dict__ for command in Commander.commands])
            with open("visualization.json", "w") as file:
                file.write(content)
        except Exception as e:
            print(f"Error occurred: {e}", file=sys.stderr)


def shutdown_hook():
    Commander.save_commands()

# 注册退出钩子
atexit.register(shutdown_hook)
