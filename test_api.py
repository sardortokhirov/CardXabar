import sys
sys.path.insert(0, r'C:\Users\Sardor\Desktop')

# Mock test
import asyncio
from main import list_active, init_db

async def test():
    init_db()
    try:
        result = await list_active(include_photo=False)
        print(f"SUCCESS: /active returned {len(result)} items")
        print(result)
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

asyncio.run(test())
