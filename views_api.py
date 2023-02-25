from python_utils import format_time
from . import dependencies_ext


# You can now use your packages as you wish
@dependencies_ext.get("/api/v1/format")
async def api_example(seconds: int):
    return format_time(seconds)
