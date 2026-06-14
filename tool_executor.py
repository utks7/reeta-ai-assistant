from actions.utility_actions import tell_time, tell_joke
from actions.web_actions import open_youtube, search_google
from actions.app_actions import open_application
from actions.knowledge_actions import tell_about


def execute_tool(tool_name, command=""):

    tool_name = tool_name.lower()

    if tool_name == "tell_time":
        tell_time()

    elif tool_name == "tell_joke":
        tell_joke()

    elif tool_name == "open_youtube":
        open_youtube()

    elif tool_name == "search_google":
        search_google(command)

    elif tool_name == "open_application":
        open_application(command)

    elif tool_name == "tell_about":
        tell_about(command)

    else:
        raise ValueError(f"Unknown tool: {tool_name}")