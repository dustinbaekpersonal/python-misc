"""
Online cloud reading app
Similar to amazon kindle
Need to implement this app

Featuers:
1. users have a library of books that they can
    add to or remove from
2. users can set a book from their library as active
3. app remembers where a user left off in a give book
4. app only displays a page of text at a time
    in the active book
    
Objects needed:
1. app object
    remember last page
    display one page
2. library object
    active
    set, because same book can't be in one library
    
    
    
3. book object
    attr:
        title (str)
        pages (list of strings or tuple because it's immutable)
        last page (int): pages[int], careful with indexing (should start from 1)
        status (active or not)
4. page object


"""
import random
import logging
import sys

logging.basicConfig(filename="example.log", level=logging.INFO)
pages_tuple = ("asdf", "asdf", "asdf")
pages_list = ["asdf", "asdf", "asdf"]

logging.info(f"size of list in byte: {sys.getsizeof(pages_list)}")
logging.info(f"size of tuple in byte: {sys.getsizeof(pages_tuple)}")

id = hash(pages_list[0])
logging.info(f"size of hash {id} in byte: {sys.getsizeof(id)}")
id = hash(pages_list[1])
logging.info(f"size of integer {id} in byte: {sys.getsizeof(id)}")
