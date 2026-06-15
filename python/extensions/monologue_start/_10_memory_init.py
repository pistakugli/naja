from python.helpers.extension import Extension
from agent import LoopData


class MemoryInit(Extension):

    async def execute(self, loop_data: LoopData = LoopData(), **kwargs):
        pass  # Memory disabled - no embedding provider available
