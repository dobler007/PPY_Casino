from typing import Optional,List


from fastapi import FastAPI

app = FastAPI()


# Path parameters
@app.get("/add/{x}/{y}")
def add(x: float, y: float) -> float:
    return x + y

@app.post("/sort_list")
async def remove_odds(lists: List[int]):
    new = []
    for i in range(len(lists)):
        if lists[i] % 2 != 0:
            new.append(lists[i])
        else:
            pass

    return {"sorted_list": new}
