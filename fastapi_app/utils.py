async def query_parameters(tanks: int | None = None, bbms: int | None = None):
    return {"Танки": tanks, "ББМ": bbms}