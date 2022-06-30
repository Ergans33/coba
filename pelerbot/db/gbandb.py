from pelerbot.db import mongodb

gbun = mongodb.gbun


async def gban_user(user, reason="#GBanned"):
    user.id = int(user)
    gbunned = await gbun.find_one({"user": user.id})
    if gbunned:
        return True
    else:
        await gbun.insert_one({"user": user.id, "reason": reason})


async def ungban_user(user):
    await gbun.delete_one({"user": user})


async def gban_list():
    return [lo async for lo in gbun.find({})]


async def gban_info(user):
    kk = await gbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]
