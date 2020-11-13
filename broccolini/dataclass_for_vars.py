#     """Dataclass used for sharing data.  also base for fastapi and async."""
# from typing import Optional  # Optional allows variable to contain "none"the data type
# from fastapi import FastAPI  # Calling the FastAPI library
# import aiofiles
# from pydantic import BaseModel

# class DnfTransaction(BaseModel):
#     id: int
#     command: str
#     date: str

# # async def read_history():
# #     transactions = []
#     async with aiofiles.open("history.txt") as f:
#         async for line in f:
#             transactions.append(
#                 DnfTransaction(
#                     id=line.split("|")[0].strip(" "),
#                     command=line.split("|")[1].strip(" "),
#                     date=line.split("|")[2].strip(" "),
#                 )
#             )
#     return transactions
